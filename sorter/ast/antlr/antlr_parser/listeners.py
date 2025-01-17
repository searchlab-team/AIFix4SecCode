from .JavaParserListener import JavaParserListener
from .JavaParser import JavaParser

class PrintListener(JavaParserListener):
	def __init__(self):
		self.indent = 0
	def enterCompilationUnit(self, ctx:JavaParser.CompilationUnitContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitCompilationUnit(self, ctx:JavaParser.CompilationUnitContext):
		self.indent -= 4

	def enterPackageDeclaration(self, ctx:JavaParser.PackageDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitPackageDeclaration(self, ctx:JavaParser.PackageDeclarationContext):
		self.indent -= 4

	def enterImportDeclaration(self, ctx:JavaParser.ImportDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitImportDeclaration(self, ctx:JavaParser.ImportDeclarationContext):
		self.indent -= 4

	def enterClassDeclaration(self, ctx:JavaParser.ClassDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitClassDeclaration(self, ctx:JavaParser.ClassDeclarationContext):
		self.indent -= 4

	def enterTypeParameter(self, ctx:JavaParser.TypeParameterContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitTypeParameter(self, ctx:JavaParser.TypeParameterContext):
		self.indent -= 4

	def enterTypeBound(self, ctx:JavaParser.TypeBoundContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitTypeBound(self, ctx:JavaParser.TypeBoundContext):
		self.indent -= 4

	def enterEnumDeclaration(self, ctx:JavaParser.EnumDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitEnumDeclaration(self, ctx:JavaParser.EnumDeclarationContext):
		self.indent -= 4

	def enterEnumConstants(self, ctx:JavaParser.EnumConstantsContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitEnumConstants(self, ctx:JavaParser.EnumConstantsContext):
		self.indent -= 4

	def enterEnumConstant(self, ctx:JavaParser.EnumConstantContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitEnumConstant(self, ctx:JavaParser.EnumConstantContext):
		self.indent -= 4

	def enterInterfaceDeclaration(self, ctx:JavaParser.InterfaceDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitInterfaceDeclaration(self, ctx:JavaParser.InterfaceDeclarationContext):
		self.indent -= 4

	def enterMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
		self.indent -= 4

	def enterGenericMethodDeclaration(self, ctx:JavaParser.GenericMethodDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitGenericMethodDeclaration(self, ctx:JavaParser.GenericMethodDeclarationContext):
		self.indent -= 4

	def enterGenericConstructorDeclaration(self, ctx:JavaParser.GenericConstructorDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitGenericConstructorDeclaration(self, ctx:JavaParser.GenericConstructorDeclarationContext):
		self.indent -= 4

	def enterConstructorDeclaration(self, ctx:JavaParser.ConstructorDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitConstructorDeclaration(self, ctx:JavaParser.ConstructorDeclarationContext):
		self.indent -= 4

	def enterFieldDeclaration(self, ctx:JavaParser.FieldDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitFieldDeclaration(self, ctx:JavaParser.FieldDeclarationContext):
		self.indent -= 4

	def enterConstDeclaration(self, ctx:JavaParser.ConstDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitConstDeclaration(self, ctx:JavaParser.ConstDeclarationContext):
		self.indent -= 4

	def enterConstantDeclarator(self, ctx:JavaParser.ConstantDeclaratorContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitConstantDeclarator(self, ctx:JavaParser.ConstantDeclaratorContext):
		self.indent -= 4

	def enterInterfaceMethodDeclaration(self, ctx:JavaParser.InterfaceMethodDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitInterfaceMethodDeclaration(self, ctx:JavaParser.InterfaceMethodDeclarationContext):
		self.indent -= 4

	def enterGenericInterfaceMethodDeclaration(self, ctx:JavaParser.GenericInterfaceMethodDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitGenericInterfaceMethodDeclaration(self, ctx:JavaParser.GenericInterfaceMethodDeclarationContext):
		self.indent -= 4

	def enterVariableDeclarator(self, ctx:JavaParser.VariableDeclaratorContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitVariableDeclarator(self, ctx:JavaParser.VariableDeclaratorContext):
		self.indent -= 4

	def enterVariableInitializer(self, ctx:JavaParser.VariableInitializerContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitVariableInitializer(self, ctx:JavaParser.VariableInitializerContext):
		self.indent -= 4

	def enterArrayInitializer(self, ctx:JavaParser.ArrayInitializerContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitArrayInitializer(self, ctx:JavaParser.ArrayInitializerContext):
		self.indent -= 4

	def enterTypeArgument(self, ctx:JavaParser.TypeArgumentContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitTypeArgument(self, ctx:JavaParser.TypeArgumentContext):
		self.indent -= 4

	def enterQualifiedNameList(self, ctx:JavaParser.QualifiedNameListContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitQualifiedNameList(self, ctx:JavaParser.QualifiedNameListContext):
		self.indent -= 4

	def enterReceiverParameter(self, ctx:JavaParser.ReceiverParameterContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitReceiverParameter(self, ctx:JavaParser.ReceiverParameterContext):
		self.indent -= 4

	def enterFormalParameter(self, ctx:JavaParser.FormalParameterContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitFormalParameter(self, ctx:JavaParser.FormalParameterContext):
		self.indent -= 4

	def enterLastFormalParameter(self, ctx:JavaParser.LastFormalParameterContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitLastFormalParameter(self, ctx:JavaParser.LastFormalParameterContext):
		self.indent -= 4

	def enterLambdaLVTIParameter(self, ctx:JavaParser.LambdaLVTIParameterContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitLambdaLVTIParameter(self, ctx:JavaParser.LambdaLVTIParameterContext):
		self.indent -= 4

	def enterQualifiedName(self, ctx:JavaParser.QualifiedNameContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitQualifiedName(self, ctx:JavaParser.QualifiedNameContext):
		self.indent -= 4

	def enterLiteral(self, ctx:JavaParser.LiteralContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitLiteral(self, ctx:JavaParser.LiteralContext):
		self.indent -= 4

	def enterIntegerLiteral(self, ctx:JavaParser.IntegerLiteralContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitIntegerLiteral(self, ctx:JavaParser.IntegerLiteralContext):
		self.indent -= 4

	def enterFloatLiteral(self, ctx:JavaParser.FloatLiteralContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitFloatLiteral(self, ctx:JavaParser.FloatLiteralContext):
		self.indent -= 4

	def enterAltAnnotationQualifiedName(self, ctx:JavaParser.AltAnnotationQualifiedNameContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitAltAnnotationQualifiedName(self, ctx:JavaParser.AltAnnotationQualifiedNameContext):
		self.indent -= 4

	def enterAnnotation(self, ctx:JavaParser.AnnotationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitAnnotation(self, ctx:JavaParser.AnnotationContext):
		self.indent -= 4

	def enterElementValuePairs(self, ctx:JavaParser.ElementValuePairsContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitElementValuePairs(self, ctx:JavaParser.ElementValuePairsContext):
		self.indent -= 4

	def enterElementValuePair(self, ctx:JavaParser.ElementValuePairContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitElementValuePair(self, ctx:JavaParser.ElementValuePairContext):
		self.indent -= 4

	def enterElementValue(self, ctx:JavaParser.ElementValueContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitElementValue(self, ctx:JavaParser.ElementValueContext):
		self.indent -= 4

	def enterElementValueArrayInitializer(self, ctx:JavaParser.ElementValueArrayInitializerContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitElementValueArrayInitializer(self, ctx:JavaParser.ElementValueArrayInitializerContext):
		self.indent -= 4

	def enterAnnotationTypeDeclaration(self, ctx:JavaParser.AnnotationTypeDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitAnnotationTypeDeclaration(self, ctx:JavaParser.AnnotationTypeDeclarationContext):
		self.indent -= 4

	def enterAnnotationTypeElementDeclaration(self, ctx:JavaParser.AnnotationTypeElementDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitAnnotationTypeElementDeclaration(self, ctx:JavaParser.AnnotationTypeElementDeclarationContext):
		self.indent -= 4

	def enterAnnotationTypeElementRest(self, ctx:JavaParser.AnnotationTypeElementRestContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitAnnotationTypeElementRest(self, ctx:JavaParser.AnnotationTypeElementRestContext):
		self.indent -= 4

	def enterAnnotationMethodOrConstantRest(self, ctx:JavaParser.AnnotationMethodOrConstantRestContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitAnnotationMethodOrConstantRest(self, ctx:JavaParser.AnnotationMethodOrConstantRestContext):
		self.indent -= 4

	def enterAnnotationMethodRest(self, ctx:JavaParser.AnnotationMethodRestContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitAnnotationMethodRest(self, ctx:JavaParser.AnnotationMethodRestContext):
		self.indent -= 4

	def enterAnnotationConstantRest(self, ctx:JavaParser.AnnotationConstantRestContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitAnnotationConstantRest(self, ctx:JavaParser.AnnotationConstantRestContext):
		self.indent -= 4

	def enterDefaultValue(self, ctx:JavaParser.DefaultValueContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitDefaultValue(self, ctx:JavaParser.DefaultValueContext):
		self.indent -= 4

	def enterModuleDeclaration(self, ctx:JavaParser.ModuleDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitModuleDeclaration(self, ctx:JavaParser.ModuleDeclarationContext):
		self.indent -= 4

	def enterModuleDirective(self, ctx:JavaParser.ModuleDirectiveContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitModuleDirective(self, ctx:JavaParser.ModuleDirectiveContext):
		self.indent -= 4

	def enterRequiresModifier(self, ctx:JavaParser.RequiresModifierContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitRequiresModifier(self, ctx:JavaParser.RequiresModifierContext):
		self.indent -= 4

	def enterRecordDeclaration(self, ctx:JavaParser.RecordDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitRecordDeclaration(self, ctx:JavaParser.RecordDeclarationContext):
		self.indent -= 4

	def enterRecordHeader(self, ctx:JavaParser.RecordHeaderContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitRecordHeader(self, ctx:JavaParser.RecordHeaderContext):
		self.indent -= 4

	def enterRecordComponentList(self, ctx:JavaParser.RecordComponentListContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitRecordComponentList(self, ctx:JavaParser.RecordComponentListContext):
		self.indent -= 4

	def enterRecordComponent(self, ctx:JavaParser.RecordComponentContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitRecordComponent(self, ctx:JavaParser.RecordComponentContext):
		self.indent -= 4

	def enterLocalVariableDeclaration(self, ctx:JavaParser.LocalVariableDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitLocalVariableDeclaration(self, ctx:JavaParser.LocalVariableDeclarationContext):
		self.indent -= 4

	def enterLocalTypeDeclaration(self, ctx:JavaParser.LocalTypeDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitLocalTypeDeclaration(self, ctx:JavaParser.LocalTypeDeclarationContext):
		self.indent -= 4

	def enterStatement(self, ctx:JavaParser.StatementContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitStatement(self, ctx:JavaParser.StatementContext):
		self.indent -= 4

	def enterCatchClause(self, ctx:JavaParser.CatchClauseContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitCatchClause(self, ctx:JavaParser.CatchClauseContext):
		self.indent -= 4

	def enterCatchType(self, ctx:JavaParser.CatchTypeContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitCatchType(self, ctx:JavaParser.CatchTypeContext):
		self.indent -= 4

	def enterFinallyBlock(self, ctx:JavaParser.FinallyBlockContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitFinallyBlock(self, ctx:JavaParser.FinallyBlockContext):
		self.indent -= 4

	def enterResourceSpecification(self, ctx:JavaParser.ResourceSpecificationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitResourceSpecification(self, ctx:JavaParser.ResourceSpecificationContext):
		self.indent -= 4

	def enterResources(self, ctx:JavaParser.ResourcesContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitResources(self, ctx:JavaParser.ResourcesContext):
		self.indent -= 4

	def enterResource(self, ctx:JavaParser.ResourceContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitResource(self, ctx:JavaParser.ResourceContext):
		self.indent -= 4

	def enterSwitchBlockStatementGroup(self, ctx:JavaParser.SwitchBlockStatementGroupContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitSwitchBlockStatementGroup(self, ctx:JavaParser.SwitchBlockStatementGroupContext):
		self.indent -= 4

	def enterSwitchLabel(self, ctx:JavaParser.SwitchLabelContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitSwitchLabel(self, ctx:JavaParser.SwitchLabelContext):
		self.indent -= 4

	def enterForControl(self, ctx:JavaParser.ForControlContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitForControl(self, ctx:JavaParser.ForControlContext):
		self.indent -= 4

	def enterForInit(self, ctx:JavaParser.ForInitContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitForInit(self, ctx:JavaParser.ForInitContext):
		self.indent -= 4

	def enterEnhancedForControl(self, ctx:JavaParser.EnhancedForControlContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitEnhancedForControl(self, ctx:JavaParser.EnhancedForControlContext):
		self.indent -= 4

	def enterParExpression(self, ctx:JavaParser.ParExpressionContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitParExpression(self, ctx:JavaParser.ParExpressionContext):
		self.indent -= 4

	def enterMethodCall(self, ctx:JavaParser.MethodCallContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitMethodCall(self, ctx:JavaParser.MethodCallContext):
		self.indent -= 4

	def enterPattern(self, ctx:JavaParser.PatternContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitPattern(self, ctx:JavaParser.PatternContext):
		self.indent -= 4

	def enterLambdaExpression(self, ctx:JavaParser.LambdaExpressionContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitLambdaExpression(self, ctx:JavaParser.LambdaExpressionContext):
		self.indent -= 4

	def enterPrimary(self, ctx:JavaParser.PrimaryContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitPrimary(self, ctx:JavaParser.PrimaryContext):
		self.indent -= 4

	def enterSwitchExpression(self, ctx:JavaParser.SwitchExpressionContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitSwitchExpression(self, ctx:JavaParser.SwitchExpressionContext):
		self.indent -= 4

	def enterSwitchLabeledRule(self, ctx:JavaParser.SwitchLabeledRuleContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitSwitchLabeledRule(self, ctx:JavaParser.SwitchLabeledRuleContext):
		self.indent -= 4

	def enterGuardedPattern(self, ctx:JavaParser.GuardedPatternContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitGuardedPattern(self, ctx:JavaParser.GuardedPatternContext):
		self.indent -= 4

	def enterSwitchRuleOutcome(self, ctx:JavaParser.SwitchRuleOutcomeContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitSwitchRuleOutcome(self, ctx:JavaParser.SwitchRuleOutcomeContext):
		self.indent -= 4

	def enterClassType(self, ctx:JavaParser.ClassTypeContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitClassType(self, ctx:JavaParser.ClassTypeContext):
		self.indent -= 4

	def enterCreator(self, ctx:JavaParser.CreatorContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitCreator(self, ctx:JavaParser.CreatorContext):
		self.indent -= 4

	def enterCreatedName(self, ctx:JavaParser.CreatedNameContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitCreatedName(self, ctx:JavaParser.CreatedNameContext):
		self.indent -= 4

	def enterInnerCreator(self, ctx:JavaParser.InnerCreatorContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitInnerCreator(self, ctx:JavaParser.InnerCreatorContext):
		self.indent -= 4

	def enterArrayCreatorRest(self, ctx:JavaParser.ArrayCreatorRestContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitArrayCreatorRest(self, ctx:JavaParser.ArrayCreatorRestContext):
		self.indent -= 4

	def enterClassCreatorRest(self, ctx:JavaParser.ClassCreatorRestContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitClassCreatorRest(self, ctx:JavaParser.ClassCreatorRestContext):
		self.indent -= 4

	def enterExplicitGenericInvocation(self, ctx:JavaParser.ExplicitGenericInvocationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitExplicitGenericInvocation(self, ctx:JavaParser.ExplicitGenericInvocationContext):
		self.indent -= 4

	def enterTypeArgumentsOrDiamond(self, ctx:JavaParser.TypeArgumentsOrDiamondContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitTypeArgumentsOrDiamond(self, ctx:JavaParser.TypeArgumentsOrDiamondContext):
		self.indent -= 4

	def enterNonWildcardTypeArgumentsOrDiamond(self, ctx:JavaParser.NonWildcardTypeArgumentsOrDiamondContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitNonWildcardTypeArgumentsOrDiamond(self, ctx:JavaParser.NonWildcardTypeArgumentsOrDiamondContext):
		self.indent -= 4

	def enterNonWildcardTypeArguments(self, ctx:JavaParser.NonWildcardTypeArgumentsContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitNonWildcardTypeArguments(self, ctx:JavaParser.NonWildcardTypeArgumentsContext):
		self.indent -= 4

	def enterTypeArguments(self, ctx:JavaParser.TypeArgumentsContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitTypeArguments(self, ctx:JavaParser.TypeArgumentsContext):
		self.indent -= 4

	def enterSuperSuffix(self, ctx:JavaParser.SuperSuffixContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitSuperSuffix(self, ctx:JavaParser.SuperSuffixContext):
		self.indent -= 4

	def enterExplicitGenericInvocationSuffix(self, ctx:JavaParser.ExplicitGenericInvocationSuffixContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitExplicitGenericInvocationSuffix(self, ctx:JavaParser.ExplicitGenericInvocationSuffixContext):
		self.indent -= 4

	def enterArguments(self, ctx:JavaParser.ArgumentsContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitArguments(self, ctx:JavaParser.ArgumentsContext):
		self.indent -= 4
class PrintAllListener(JavaParserListener):
	def __init__(self):
		self.indent = 0
	def enterCompilationUnit(self, ctx:JavaParser.CompilationUnitContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitCompilationUnit(self, ctx:JavaParser.CompilationUnitContext):
		self.indent -= 4

	def enterPackageDeclaration(self, ctx:JavaParser.PackageDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitPackageDeclaration(self, ctx:JavaParser.PackageDeclarationContext):
		self.indent -= 4

	def enterImportDeclaration(self, ctx:JavaParser.ImportDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitImportDeclaration(self, ctx:JavaParser.ImportDeclarationContext):
		self.indent -= 4

	def enterTypeDeclaration(self, ctx:JavaParser.TypeDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitTypeDeclaration(self, ctx:JavaParser.TypeDeclarationContext):
		self.indent -= 4

	def enterModifier(self, ctx:JavaParser.ModifierContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitModifier(self, ctx:JavaParser.ModifierContext):
		self.indent -= 4

	def enterClassOrInterfaceModifier(self, ctx:JavaParser.ClassOrInterfaceModifierContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitClassOrInterfaceModifier(self, ctx:JavaParser.ClassOrInterfaceModifierContext):
		self.indent -= 4

	def enterVariableModifier(self, ctx:JavaParser.VariableModifierContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitVariableModifier(self, ctx:JavaParser.VariableModifierContext):
		self.indent -= 4

	def enterClassDeclaration(self, ctx:JavaParser.ClassDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitClassDeclaration(self, ctx:JavaParser.ClassDeclarationContext):
		self.indent -= 4

	def enterTypeParameters(self, ctx:JavaParser.TypeParametersContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitTypeParameters(self, ctx:JavaParser.TypeParametersContext):
		self.indent -= 4

	def enterTypeParameter(self, ctx:JavaParser.TypeParameterContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitTypeParameter(self, ctx:JavaParser.TypeParameterContext):
		self.indent -= 4

	def enterTypeBound(self, ctx:JavaParser.TypeBoundContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitTypeBound(self, ctx:JavaParser.TypeBoundContext):
		self.indent -= 4

	def enterEnumDeclaration(self, ctx:JavaParser.EnumDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitEnumDeclaration(self, ctx:JavaParser.EnumDeclarationContext):
		self.indent -= 4

	def enterEnumConstants(self, ctx:JavaParser.EnumConstantsContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitEnumConstants(self, ctx:JavaParser.EnumConstantsContext):
		self.indent -= 4

	def enterEnumConstant(self, ctx:JavaParser.EnumConstantContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitEnumConstant(self, ctx:JavaParser.EnumConstantContext):
		self.indent -= 4

	def enterEnumBodyDeclarations(self, ctx:JavaParser.EnumBodyDeclarationsContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitEnumBodyDeclarations(self, ctx:JavaParser.EnumBodyDeclarationsContext):
		self.indent -= 4

	def enterInterfaceDeclaration(self, ctx:JavaParser.InterfaceDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitInterfaceDeclaration(self, ctx:JavaParser.InterfaceDeclarationContext):
		self.indent -= 4

	def enterClassBody(self, ctx:JavaParser.ClassBodyContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitClassBody(self, ctx:JavaParser.ClassBodyContext):
		self.indent -= 4

	def enterInterfaceBody(self, ctx:JavaParser.InterfaceBodyContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitInterfaceBody(self, ctx:JavaParser.InterfaceBodyContext):
		self.indent -= 4

	def enterClassBodyDeclaration(self, ctx:JavaParser.ClassBodyDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitClassBodyDeclaration(self, ctx:JavaParser.ClassBodyDeclarationContext):
		self.indent -= 4

	def enterMemberDeclaration(self, ctx:JavaParser.MemberDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitMemberDeclaration(self, ctx:JavaParser.MemberDeclarationContext):
		self.indent -= 4

	def enterMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
		self.indent -= 4

	def enterMethodBody(self, ctx:JavaParser.MethodBodyContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitMethodBody(self, ctx:JavaParser.MethodBodyContext):
		self.indent -= 4

	def enterTypeTypeOrVoid(self, ctx:JavaParser.TypeTypeOrVoidContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitTypeTypeOrVoid(self, ctx:JavaParser.TypeTypeOrVoidContext):
		self.indent -= 4

	def enterGenericMethodDeclaration(self, ctx:JavaParser.GenericMethodDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitGenericMethodDeclaration(self, ctx:JavaParser.GenericMethodDeclarationContext):
		self.indent -= 4

	def enterGenericConstructorDeclaration(self, ctx:JavaParser.GenericConstructorDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitGenericConstructorDeclaration(self, ctx:JavaParser.GenericConstructorDeclarationContext):
		self.indent -= 4

	def enterConstructorDeclaration(self, ctx:JavaParser.ConstructorDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitConstructorDeclaration(self, ctx:JavaParser.ConstructorDeclarationContext):
		self.indent -= 4

	def enterFieldDeclaration(self, ctx:JavaParser.FieldDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitFieldDeclaration(self, ctx:JavaParser.FieldDeclarationContext):
		self.indent -= 4

	def enterInterfaceBodyDeclaration(self, ctx:JavaParser.InterfaceBodyDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitInterfaceBodyDeclaration(self, ctx:JavaParser.InterfaceBodyDeclarationContext):
		self.indent -= 4

	def enterInterfaceMemberDeclaration(self, ctx:JavaParser.InterfaceMemberDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitInterfaceMemberDeclaration(self, ctx:JavaParser.InterfaceMemberDeclarationContext):
		self.indent -= 4

	def enterConstDeclaration(self, ctx:JavaParser.ConstDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitConstDeclaration(self, ctx:JavaParser.ConstDeclarationContext):
		self.indent -= 4

	def enterConstantDeclarator(self, ctx:JavaParser.ConstantDeclaratorContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitConstantDeclarator(self, ctx:JavaParser.ConstantDeclaratorContext):
		self.indent -= 4

	def enterInterfaceMethodDeclaration(self, ctx:JavaParser.InterfaceMethodDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitInterfaceMethodDeclaration(self, ctx:JavaParser.InterfaceMethodDeclarationContext):
		self.indent -= 4

	def enterInterfaceMethodModifier(self, ctx:JavaParser.InterfaceMethodModifierContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitInterfaceMethodModifier(self, ctx:JavaParser.InterfaceMethodModifierContext):
		self.indent -= 4

	def enterGenericInterfaceMethodDeclaration(self, ctx:JavaParser.GenericInterfaceMethodDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitGenericInterfaceMethodDeclaration(self, ctx:JavaParser.GenericInterfaceMethodDeclarationContext):
		self.indent -= 4

	def enterInterfaceCommonBodyDeclaration(self, ctx:JavaParser.InterfaceCommonBodyDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitInterfaceCommonBodyDeclaration(self, ctx:JavaParser.InterfaceCommonBodyDeclarationContext):
		self.indent -= 4

	def enterVariableDeclarators(self, ctx:JavaParser.VariableDeclaratorsContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitVariableDeclarators(self, ctx:JavaParser.VariableDeclaratorsContext):
		self.indent -= 4

	def enterVariableDeclarator(self, ctx:JavaParser.VariableDeclaratorContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitVariableDeclarator(self, ctx:JavaParser.VariableDeclaratorContext):
		self.indent -= 4

	def enterVariableDeclaratorId(self, ctx:JavaParser.VariableDeclaratorIdContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitVariableDeclaratorId(self, ctx:JavaParser.VariableDeclaratorIdContext):
		self.indent -= 4

	def enterVariableInitializer(self, ctx:JavaParser.VariableInitializerContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitVariableInitializer(self, ctx:JavaParser.VariableInitializerContext):
		self.indent -= 4

	def enterArrayInitializer(self, ctx:JavaParser.ArrayInitializerContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitArrayInitializer(self, ctx:JavaParser.ArrayInitializerContext):
		self.indent -= 4

	def enterClassOrInterfaceType(self, ctx:JavaParser.ClassOrInterfaceTypeContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitClassOrInterfaceType(self, ctx:JavaParser.ClassOrInterfaceTypeContext):
		self.indent -= 4

	def enterTypeArgument(self, ctx:JavaParser.TypeArgumentContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitTypeArgument(self, ctx:JavaParser.TypeArgumentContext):
		self.indent -= 4

	def enterQualifiedNameList(self, ctx:JavaParser.QualifiedNameListContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitQualifiedNameList(self, ctx:JavaParser.QualifiedNameListContext):
		self.indent -= 4

	def enterFormalParameters(self, ctx:JavaParser.FormalParametersContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitFormalParameters(self, ctx:JavaParser.FormalParametersContext):
		self.indent -= 4

	def enterReceiverParameter(self, ctx:JavaParser.ReceiverParameterContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitReceiverParameter(self, ctx:JavaParser.ReceiverParameterContext):
		self.indent -= 4

	def enterFormalParameterList(self, ctx:JavaParser.FormalParameterListContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitFormalParameterList(self, ctx:JavaParser.FormalParameterListContext):
		self.indent -= 4

	def enterFormalParameter(self, ctx:JavaParser.FormalParameterContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitFormalParameter(self, ctx:JavaParser.FormalParameterContext):
		self.indent -= 4

	def enterLastFormalParameter(self, ctx:JavaParser.LastFormalParameterContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitLastFormalParameter(self, ctx:JavaParser.LastFormalParameterContext):
		self.indent -= 4

	def enterLambdaLVTIList(self, ctx:JavaParser.LambdaLVTIListContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitLambdaLVTIList(self, ctx:JavaParser.LambdaLVTIListContext):
		self.indent -= 4

	def enterLambdaLVTIParameter(self, ctx:JavaParser.LambdaLVTIParameterContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitLambdaLVTIParameter(self, ctx:JavaParser.LambdaLVTIParameterContext):
		self.indent -= 4

	def enterQualifiedName(self, ctx:JavaParser.QualifiedNameContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitQualifiedName(self, ctx:JavaParser.QualifiedNameContext):
		self.indent -= 4

	def enterLiteral(self, ctx:JavaParser.LiteralContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitLiteral(self, ctx:JavaParser.LiteralContext):
		self.indent -= 4

	def enterIntegerLiteral(self, ctx:JavaParser.IntegerLiteralContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitIntegerLiteral(self, ctx:JavaParser.IntegerLiteralContext):
		self.indent -= 4

	def enterFloatLiteral(self, ctx:JavaParser.FloatLiteralContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitFloatLiteral(self, ctx:JavaParser.FloatLiteralContext):
		self.indent -= 4

	def enterAltAnnotationQualifiedName(self, ctx:JavaParser.AltAnnotationQualifiedNameContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitAltAnnotationQualifiedName(self, ctx:JavaParser.AltAnnotationQualifiedNameContext):
		self.indent -= 4

	def enterAnnotation(self, ctx:JavaParser.AnnotationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitAnnotation(self, ctx:JavaParser.AnnotationContext):
		self.indent -= 4

	def enterElementValuePairs(self, ctx:JavaParser.ElementValuePairsContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitElementValuePairs(self, ctx:JavaParser.ElementValuePairsContext):
		self.indent -= 4

	def enterElementValuePair(self, ctx:JavaParser.ElementValuePairContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitElementValuePair(self, ctx:JavaParser.ElementValuePairContext):
		self.indent -= 4

	def enterElementValue(self, ctx:JavaParser.ElementValueContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitElementValue(self, ctx:JavaParser.ElementValueContext):
		self.indent -= 4

	def enterElementValueArrayInitializer(self, ctx:JavaParser.ElementValueArrayInitializerContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitElementValueArrayInitializer(self, ctx:JavaParser.ElementValueArrayInitializerContext):
		self.indent -= 4

	def enterAnnotationTypeDeclaration(self, ctx:JavaParser.AnnotationTypeDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitAnnotationTypeDeclaration(self, ctx:JavaParser.AnnotationTypeDeclarationContext):
		self.indent -= 4

	def enterAnnotationTypeBody(self, ctx:JavaParser.AnnotationTypeBodyContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitAnnotationTypeBody(self, ctx:JavaParser.AnnotationTypeBodyContext):
		self.indent -= 4

	def enterAnnotationTypeElementDeclaration(self, ctx:JavaParser.AnnotationTypeElementDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitAnnotationTypeElementDeclaration(self, ctx:JavaParser.AnnotationTypeElementDeclarationContext):
		self.indent -= 4

	def enterAnnotationTypeElementRest(self, ctx:JavaParser.AnnotationTypeElementRestContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitAnnotationTypeElementRest(self, ctx:JavaParser.AnnotationTypeElementRestContext):
		self.indent -= 4

	def enterAnnotationMethodOrConstantRest(self, ctx:JavaParser.AnnotationMethodOrConstantRestContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitAnnotationMethodOrConstantRest(self, ctx:JavaParser.AnnotationMethodOrConstantRestContext):
		self.indent -= 4

	def enterAnnotationMethodRest(self, ctx:JavaParser.AnnotationMethodRestContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitAnnotationMethodRest(self, ctx:JavaParser.AnnotationMethodRestContext):
		self.indent -= 4

	def enterAnnotationConstantRest(self, ctx:JavaParser.AnnotationConstantRestContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitAnnotationConstantRest(self, ctx:JavaParser.AnnotationConstantRestContext):
		self.indent -= 4

	def enterDefaultValue(self, ctx:JavaParser.DefaultValueContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitDefaultValue(self, ctx:JavaParser.DefaultValueContext):
		self.indent -= 4

	def enterModuleDeclaration(self, ctx:JavaParser.ModuleDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitModuleDeclaration(self, ctx:JavaParser.ModuleDeclarationContext):
		self.indent -= 4

	def enterModuleBody(self, ctx:JavaParser.ModuleBodyContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitModuleBody(self, ctx:JavaParser.ModuleBodyContext):
		self.indent -= 4

	def enterModuleDirective(self, ctx:JavaParser.ModuleDirectiveContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitModuleDirective(self, ctx:JavaParser.ModuleDirectiveContext):
		self.indent -= 4

	def enterRequiresModifier(self, ctx:JavaParser.RequiresModifierContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitRequiresModifier(self, ctx:JavaParser.RequiresModifierContext):
		self.indent -= 4

	def enterRecordDeclaration(self, ctx:JavaParser.RecordDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitRecordDeclaration(self, ctx:JavaParser.RecordDeclarationContext):
		self.indent -= 4

	def enterRecordHeader(self, ctx:JavaParser.RecordHeaderContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitRecordHeader(self, ctx:JavaParser.RecordHeaderContext):
		self.indent -= 4

	def enterRecordComponentList(self, ctx:JavaParser.RecordComponentListContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitRecordComponentList(self, ctx:JavaParser.RecordComponentListContext):
		self.indent -= 4

	def enterRecordComponent(self, ctx:JavaParser.RecordComponentContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitRecordComponent(self, ctx:JavaParser.RecordComponentContext):
		self.indent -= 4

	def enterRecordBody(self, ctx:JavaParser.RecordBodyContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitRecordBody(self, ctx:JavaParser.RecordBodyContext):
		self.indent -= 4

	def enterBlock(self, ctx:JavaParser.BlockContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitBlock(self, ctx:JavaParser.BlockContext):
		self.indent -= 4

	def enterBlockStatement(self, ctx:JavaParser.BlockStatementContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitBlockStatement(self, ctx:JavaParser.BlockStatementContext):
		self.indent -= 4

	def enterLocalVariableDeclaration(self, ctx:JavaParser.LocalVariableDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitLocalVariableDeclaration(self, ctx:JavaParser.LocalVariableDeclarationContext):
		self.indent -= 4

	def enterIdentifier(self, ctx:JavaParser.IdentifierContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitIdentifier(self, ctx:JavaParser.IdentifierContext):
		self.indent -= 4

	def enterLocalTypeDeclaration(self, ctx:JavaParser.LocalTypeDeclarationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitLocalTypeDeclaration(self, ctx:JavaParser.LocalTypeDeclarationContext):
		self.indent -= 4

	def enterStatement(self, ctx:JavaParser.StatementContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitStatement(self, ctx:JavaParser.StatementContext):
		self.indent -= 4

	def enterCatchClause(self, ctx:JavaParser.CatchClauseContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitCatchClause(self, ctx:JavaParser.CatchClauseContext):
		self.indent -= 4

	def enterCatchType(self, ctx:JavaParser.CatchTypeContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitCatchType(self, ctx:JavaParser.CatchTypeContext):
		self.indent -= 4

	def enterFinallyBlock(self, ctx:JavaParser.FinallyBlockContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitFinallyBlock(self, ctx:JavaParser.FinallyBlockContext):
		self.indent -= 4

	def enterResourceSpecification(self, ctx:JavaParser.ResourceSpecificationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitResourceSpecification(self, ctx:JavaParser.ResourceSpecificationContext):
		self.indent -= 4

	def enterResources(self, ctx:JavaParser.ResourcesContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitResources(self, ctx:JavaParser.ResourcesContext):
		self.indent -= 4

	def enterResource(self, ctx:JavaParser.ResourceContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitResource(self, ctx:JavaParser.ResourceContext):
		self.indent -= 4

	def enterSwitchBlockStatementGroup(self, ctx:JavaParser.SwitchBlockStatementGroupContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitSwitchBlockStatementGroup(self, ctx:JavaParser.SwitchBlockStatementGroupContext):
		self.indent -= 4

	def enterSwitchLabel(self, ctx:JavaParser.SwitchLabelContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitSwitchLabel(self, ctx:JavaParser.SwitchLabelContext):
		self.indent -= 4

	def enterForControl(self, ctx:JavaParser.ForControlContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitForControl(self, ctx:JavaParser.ForControlContext):
		self.indent -= 4

	def enterForInit(self, ctx:JavaParser.ForInitContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitForInit(self, ctx:JavaParser.ForInitContext):
		self.indent -= 4

	def enterEnhancedForControl(self, ctx:JavaParser.EnhancedForControlContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitEnhancedForControl(self, ctx:JavaParser.EnhancedForControlContext):
		self.indent -= 4

	def enterParExpression(self, ctx:JavaParser.ParExpressionContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitParExpression(self, ctx:JavaParser.ParExpressionContext):
		self.indent -= 4

	def enterExpressionList(self, ctx:JavaParser.ExpressionListContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitExpressionList(self, ctx:JavaParser.ExpressionListContext):
		self.indent -= 4

	def enterMethodCall(self, ctx:JavaParser.MethodCallContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitMethodCall(self, ctx:JavaParser.MethodCallContext):
		self.indent -= 4

	def enterExpression(self, ctx:JavaParser.ExpressionContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitExpression(self, ctx:JavaParser.ExpressionContext):
		self.indent -= 4

	def enterPattern(self, ctx:JavaParser.PatternContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitPattern(self, ctx:JavaParser.PatternContext):
		self.indent -= 4

	def enterLambdaExpression(self, ctx:JavaParser.LambdaExpressionContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitLambdaExpression(self, ctx:JavaParser.LambdaExpressionContext):
		self.indent -= 4

	def enterLambdaParameters(self, ctx:JavaParser.LambdaParametersContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitLambdaParameters(self, ctx:JavaParser.LambdaParametersContext):
		self.indent -= 4

	def enterLambdaBody(self, ctx:JavaParser.LambdaBodyContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitLambdaBody(self, ctx:JavaParser.LambdaBodyContext):
		self.indent -= 4

	def enterPrimary(self, ctx:JavaParser.PrimaryContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitPrimary(self, ctx:JavaParser.PrimaryContext):
		self.indent -= 4

	def enterSwitchExpression(self, ctx:JavaParser.SwitchExpressionContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitSwitchExpression(self, ctx:JavaParser.SwitchExpressionContext):
		self.indent -= 4

	def enterSwitchLabeledRule(self, ctx:JavaParser.SwitchLabeledRuleContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitSwitchLabeledRule(self, ctx:JavaParser.SwitchLabeledRuleContext):
		self.indent -= 4

	def enterGuardedPattern(self, ctx:JavaParser.GuardedPatternContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitGuardedPattern(self, ctx:JavaParser.GuardedPatternContext):
		self.indent -= 4

	def enterSwitchRuleOutcome(self, ctx:JavaParser.SwitchRuleOutcomeContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitSwitchRuleOutcome(self, ctx:JavaParser.SwitchRuleOutcomeContext):
		self.indent -= 4

	def enterClassType(self, ctx:JavaParser.ClassTypeContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitClassType(self, ctx:JavaParser.ClassTypeContext):
		self.indent -= 4

	def enterCreator(self, ctx:JavaParser.CreatorContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitCreator(self, ctx:JavaParser.CreatorContext):
		self.indent -= 4

	def enterCreatedName(self, ctx:JavaParser.CreatedNameContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitCreatedName(self, ctx:JavaParser.CreatedNameContext):
		self.indent -= 4

	def enterInnerCreator(self, ctx:JavaParser.InnerCreatorContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitInnerCreator(self, ctx:JavaParser.InnerCreatorContext):
		self.indent -= 4

	def enterArrayCreatorRest(self, ctx:JavaParser.ArrayCreatorRestContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitArrayCreatorRest(self, ctx:JavaParser.ArrayCreatorRestContext):
		self.indent -= 4

	def enterClassCreatorRest(self, ctx:JavaParser.ClassCreatorRestContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitClassCreatorRest(self, ctx:JavaParser.ClassCreatorRestContext):
		self.indent -= 4

	def enterExplicitGenericInvocation(self, ctx:JavaParser.ExplicitGenericInvocationContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitExplicitGenericInvocation(self, ctx:JavaParser.ExplicitGenericInvocationContext):
		self.indent -= 4

	def enterTypeArgumentsOrDiamond(self, ctx:JavaParser.TypeArgumentsOrDiamondContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitTypeArgumentsOrDiamond(self, ctx:JavaParser.TypeArgumentsOrDiamondContext):
		self.indent -= 4

	def enterNonWildcardTypeArgumentsOrDiamond(self, ctx:JavaParser.NonWildcardTypeArgumentsOrDiamondContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitNonWildcardTypeArgumentsOrDiamond(self, ctx:JavaParser.NonWildcardTypeArgumentsOrDiamondContext):
		self.indent -= 4

	def enterNonWildcardTypeArguments(self, ctx:JavaParser.NonWildcardTypeArgumentsContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitNonWildcardTypeArguments(self, ctx:JavaParser.NonWildcardTypeArgumentsContext):
		self.indent -= 4

	def enterTypeList(self, ctx:JavaParser.TypeListContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitTypeList(self, ctx:JavaParser.TypeListContext):
		self.indent -= 4

	def enterTypeType(self, ctx:JavaParser.TypeTypeContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitTypeType(self, ctx:JavaParser.TypeTypeContext):
		self.indent -= 4

	def enterPrimitiveType(self, ctx:JavaParser.PrimitiveTypeContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitPrimitiveType(self, ctx:JavaParser.PrimitiveTypeContext):
		self.indent -= 4

	def enterTypeArguments(self, ctx:JavaParser.TypeArgumentsContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitTypeArguments(self, ctx:JavaParser.TypeArgumentsContext):
		self.indent -= 4

	def enterSuperSuffix(self, ctx:JavaParser.SuperSuffixContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitSuperSuffix(self, ctx:JavaParser.SuperSuffixContext):
		self.indent -= 4

	def enterExplicitGenericInvocationSuffix(self, ctx:JavaParser.ExplicitGenericInvocationSuffixContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitExplicitGenericInvocationSuffix(self, ctx:JavaParser.ExplicitGenericInvocationSuffixContext):
		self.indent -= 4

	def enterArguments(self, ctx:JavaParser.ArgumentsContext):
		print(" "*(self.indent-4)+"-"*(0 if self.indent < 4 else 4) + ctx.__class__.__name__)
		self.indent += 4

	def exitArguments(self, ctx:JavaParser.ArgumentsContext):
		self.indent -= 4
