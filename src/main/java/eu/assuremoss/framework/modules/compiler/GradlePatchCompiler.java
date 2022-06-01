package eu.assuremoss.framework.modules.compiler;

import com.github.difflib.patch.Patch;
import eu.assuremoss.utils.Pair;
import org.apache.log4j.LogManager;
import org.apache.log4j.Logger;

import java.io.*;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class GradlePatchCompiler extends GenericPatchCompiler{
    private static final Logger LOG = LogManager.getLogger(GradlePatchCompiler.class);

    @Override
    public boolean compile(File srcLocation, boolean runTests, boolean copyDependencies) {
        String path = srcLocation.getAbsolutePath();
        String command = "gradle clean build";

        if (!runTests) {
            command += " -x test";
        }

        if (copyDependencies) {
            boolean fileContainsTask = false;
            try {
                Files.deleteIfExists(Paths.get(srcLocation.getAbsolutePath(),"dependecies"));
                File myObj = new File(srcLocation.getAbsolutePath() + "\\build.gradle");
                Scanner myReader = new Scanner(myObj);

                while (myReader.hasNextLine()) {
                    String data = myReader.nextLine();
                    if(data.contains("copyDependencies")){
                        fileContainsTask = true;
                    }
                }
                myReader.close();
            } catch (FileNotFoundException e) {
                LOG.error(e);
                return false;
            } catch (IOException e) {
                LOG.error(e);
                return false;
            }
            if(!fileContainsTask) {
                try {
                    BufferedWriter out = new BufferedWriter(
                            new FileWriter(srcLocation.getAbsolutePath() + "\\build.gradle", true));
                    out.write("\n" +
                            "apply plugin: 'java'\n" +
                            "\n" +
                            "repositories {\n" +
                            "   mavenCentral()\n" +
                            "}\n" +
                            "\n" +
                            "dependencies {\n" +
                            "   compile 'com.google.inject:guice:4.0-beta5'\n" +
                            "}\n" +
                            "\n" +
                            "task copyDependencies(type: Copy) {\n" +
                            "  from configurations.default\n" +
                            "  into 'dependencies'\n" +
                            "}");
                    out.close();
                } catch (IOException e) {
                    LOG.error(e);
                    return false;
                }
            }
            command += " copyDependencies";
        }

        ProcessBuilder builder = new ProcessBuilder(
                "cmd.exe", "/c", "cd " + path + " && " + command);

        try {
            Process p = builder.start();
            BufferedReader r = new BufferedReader(new InputStreamReader(p.getInputStream()));
            String line = r.readLine();
            while (line != null) {
                if (line.contains("BUILD SUCCESSFUL")) {
                    return true;
                }
                line = r.readLine();
            }
        } catch (UnsupportedEncodingException e) {
            LOG.error(e.getMessage());
        } catch (IOException e){
            LOG.error(e.getMessage());
        }
        return false;
    }

    @Override
    public List<Pair<File, Pair<Patch<String>, String>>> applyAndCompile(File srcLocation, List<Pair<File, Pair<Patch<String>, String>>> patches, boolean runTests) {
        List<Pair<File, Pair<Patch<String>, String>>> filteredPatches = new ArrayList<>();

        for (Pair<File, Pair<Patch<String>, String>> patchWithExplanation : patches) {
            Patch<String> rawPatch = patchWithExplanation.getB().getA();
            Pair<File, Patch<String>> patch = new Pair<>(patchWithExplanation.getA(), rawPatch);
            applyPatch(patch, srcLocation);
            if (compile(srcLocation, runTests, false)) {
                filteredPatches.add(patchWithExplanation);
            }
            revertPatch(patch, srcLocation);
        }

        return filteredPatches;
    }
}
