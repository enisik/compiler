// Generated from /home/ensar/Documents/Compilerbau/compiler/GoParser.g4 by ANTLR 4.9.2

global_scope = dict()

import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class GoParser extends GoASTParser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		VAR=1, RETURN=2, FUNC=3, PACKAGE=4, IMPORT=5, IF=6, ELSE=7, FOR=8, INT_TYPE=9, 
		FLOAT_TYPE=10, BOOL_TYPE=11, STRING_TYPE=12, PLUS=13, MINUS=14, STAR=15, 
		DIVISON=16, MODULO=17, EQUALS=18, UNEQUAL=19, LESS=20, GREATER=21, LESSEQUAL=22, 
		GREATEREQUAL=23, AND=24, OR=25, NOT=26, INTEGER=27, FLOAT=28, BOOL=29, 
		STRING=30, NL=31, LB=32, RB=33, CLB=34, CRB=35, COMMA=36, DOT=37, SEMICOLON=38, 
		ASSIGN=39, WHITESPACE=40, COMMENT=41, IDENTIFIER=42;
	public static final int
		RULE_program = 0, RULE_main_function = 1, RULE_functions = 2, RULE_function = 3, 
		RULE_body = 4, RULE_func_args = 5, RULE_type = 6, RULE_declarations = 7, 
		RULE_declaration = 8, RULE_statements = 9, RULE_statement = 10, RULE_block_stmt = 11, 
		RULE_assignment = 12, RULE_if_control = 13, RULE_for_loop = 14, RULE_func_call = 15, 
		RULE_expr = 16, RULE_literals = 17;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "main_function", "functions", "function", "body", "func_args", 
			"type", "declarations", "declaration", "statements", "statement", "block_stmt", 
			"assignment", "if_control", "for_loop", "func_call", "expr", "literals"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'var'", "'return'", "'func'", "'package'", "'import'", "'if'", 
			"'else'", "'for'", "'int'", "'float64'", "'bool'", "'string'", "'+'", 
			"'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
			"'&&'", "'||'", "'!'", null, null, null, null, null, "'('", "')'", "'{'", 
			"'}'", "','", "'.'", "';'", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "VAR", "RETURN", "FUNC", "PACKAGE", "IMPORT", "IF", "ELSE", "FOR", 
			"INT_TYPE", "FLOAT_TYPE", "BOOL_TYPE", "STRING_TYPE", "PLUS", "MINUS", 
			"STAR", "DIVISON", "MODULO", "EQUALS", "UNEQUAL", "LESS", "GREATER", 
			"LESSEQUAL", "GREATEREQUAL", "AND", "OR", "NOT", "INTEGER", "FLOAT", 
			"BOOL", "STRING", "NL", "LB", "RB", "CLB", "CRB", "COMMA", "DOT", "SEMICOLON", 
			"ASSIGN", "WHITESPACE", "COMMENT", "IDENTIFIER"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "GoParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public GoParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public  ast;
		public  global_scope;
		public Token IDENTIFIER;
		public Main_functionContext main_function;
		public FunctionsContext functions;
		public TerminalNode PACKAGE() { return getToken(GoParser.PACKAGE, 0); }
		public TerminalNode IDENTIFIER() { return getToken(GoParser.IDENTIFIER, 0); }
		public List<TerminalNode> NL() { return getTokens(GoParser.NL); }
		public TerminalNode NL(int i) {
			return getToken(GoParser.NL, i);
		}
		public Main_functionContext main_function() {
			return getRuleContext(Main_functionContext.class,0);
		}
		public TerminalNode EOF() { return getToken(GoParser.EOF, 0); }
		public List<TerminalNode> IMPORT() { return getTokens(GoParser.IMPORT); }
		public TerminalNode IMPORT(int i) {
			return getToken(GoParser.IMPORT, i);
		}
		public List<TerminalNode> STRING() { return getTokens(GoParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(GoParser.STRING, i);
		}
		public FunctionsContext functions() {
			return getRuleContext(FunctionsContext.class,0);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			match(PACKAGE);
			setState(37);
			((ProgramContext)_localctx).IDENTIFIER = match(IDENTIFIER);
			setState(38);
			if (!((((ProgramContext)_localctx).IDENTIFIER!=null?((ProgramContext)_localctx).IDENTIFIER.getText():null) == "main" )) throw new FailedPredicateException(this, "$IDENTIFIER.text == \"main\" ");
			setState(39);
			match(NL);
			setState(44);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==IMPORT) {
				{
				{
				setState(40);
				match(IMPORT);
				setState(41);
				match(STRING);
				}
				}
				setState(46);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(47);
			match(NL);
			setState(48);
			((ProgramContext)_localctx).main_function = main_function();
			setState(53);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(49);
				match(NL);
				setState(50);
				((ProgramContext)_localctx).functions = functions();
				_localctx.ast = ((ProgramContext)_localctx).functions.node
				}
				break;
			}
			setState(56);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(55);
				match(NL);
				}
			}

			setState(58);
			match(EOF);
			_localctx.ast = self.ast(((ProgramContext)_localctx).main_function.node, _localctx.ast)
			_localctx.global_scope = global_scope
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Main_functionContext extends ParserRuleContext {
		public  node;
		public Token IDENTIFIER;
		public BodyContext body;
		public TerminalNode FUNC() { return getToken(GoParser.FUNC, 0); }
		public TerminalNode IDENTIFIER() { return getToken(GoParser.IDENTIFIER, 0); }
		public TerminalNode LB() { return getToken(GoParser.LB, 0); }
		public TerminalNode RB() { return getToken(GoParser.RB, 0); }
		public TerminalNode CLB() { return getToken(GoParser.CLB, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public TerminalNode CRB() { return getToken(GoParser.CRB, 0); }
		public List<TerminalNode> NL() { return getTokens(GoParser.NL); }
		public TerminalNode NL(int i) {
			return getToken(GoParser.NL, i);
		}
		public Main_functionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main_function; }
	}

	public final Main_functionContext main_function() throws RecognitionException {
		Main_functionContext _localctx = new Main_functionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_main_function);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			match(FUNC);
			setState(62);
			((Main_functionContext)_localctx).IDENTIFIER = match(IDENTIFIER);
			setState(63);
			if (!((((Main_functionContext)_localctx).IDENTIFIER!=null?((Main_functionContext)_localctx).IDENTIFIER.getText():null) == "main" )) throw new FailedPredicateException(this, "$IDENTIFIER.text == \"main\" ");
			setState(64);
			match(LB);
			setState(65);
			match(RB);
			setState(67);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(66);
				match(NL);
				}
			}

			setState(69);
			match(CLB);
			setState(71);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(70);
				match(NL);
				}
				break;
			}
			setState(73);
			((Main_functionContext)_localctx).body = body();
			setState(75);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(74);
				match(NL);
				}
			}

			setState(77);
			match(CRB);
			_localctx.node = self.funcNode('main',None, ((Main_functionContext)_localctx).body.node)
			global_scope['main'] = (None,None)
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionsContext extends ParserRuleContext {
		public  node;
		public FunctionContext function;
		public FunctionsContext functions;
		public FunctionContext function() {
			return getRuleContext(FunctionContext.class,0);
		}
		public TerminalNode NL() { return getToken(GoParser.NL, 0); }
		public FunctionsContext functions() {
			return getRuleContext(FunctionsContext.class,0);
		}
		public FunctionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functions; }
	}

	public final FunctionsContext functions() throws RecognitionException {
		FunctionsContext _localctx = new FunctionsContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_functions);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			((FunctionsContext)_localctx).function = function();
			setState(85);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				setState(81);
				match(NL);
				setState(82);
				((FunctionsContext)_localctx).functions = functions();
				_localctx.node = ((FunctionsContext)_localctx).functions.node
				}
				break;
			}
			_localctx.node = self.blockNode(((FunctionsContext)_localctx).function.node, _localctx.node)

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionContext extends ParserRuleContext {
		public  node;
		public  args;
		public  ret;
		public Token IDENTIFIER;
		public Func_argsContext func_args;
		public TypeContext type;
		public BodyContext body;
		public TerminalNode FUNC() { return getToken(GoParser.FUNC, 0); }
		public TerminalNode IDENTIFIER() { return getToken(GoParser.IDENTIFIER, 0); }
		public TerminalNode LB() { return getToken(GoParser.LB, 0); }
		public TerminalNode RB() { return getToken(GoParser.RB, 0); }
		public TerminalNode CLB() { return getToken(GoParser.CLB, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public TerminalNode CRB() { return getToken(GoParser.CRB, 0); }
		public Func_argsContext func_args() {
			return getRuleContext(Func_argsContext.class,0);
		}
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public List<TerminalNode> NL() { return getTokens(GoParser.NL); }
		public TerminalNode NL(int i) {
			return getToken(GoParser.NL, i);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_function);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			match(FUNC);
			setState(90);
			((FunctionContext)_localctx).IDENTIFIER = match(IDENTIFIER);
			setState(91);
			match(LB);
			setState(95);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IDENTIFIER) {
				{
				setState(92);
				((FunctionContext)_localctx).func_args = func_args();
				_localctx.args = ((FunctionContext)_localctx).func_args.args
				}
			}

			setState(97);
			match(RB);
			setState(101);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT_TYPE) | (1L << FLOAT_TYPE) | (1L << BOOL_TYPE) | (1L << STRING_TYPE))) != 0)) {
				{
				setState(98);
				((FunctionContext)_localctx).type = type();
				_localctx.ret = ((FunctionContext)_localctx).type.text
				}
			}

			setState(104);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(103);
				match(NL);
				}
			}

			setState(106);
			match(CLB);
			setState(108);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				{
				setState(107);
				match(NL);
				}
				break;
			}
			setState(110);
			((FunctionContext)_localctx).body = body();
			setState(112);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(111);
				match(NL);
				}
			}

			setState(114);
			match(CRB);
			_localctx.node = self.funcNode((((FunctionContext)_localctx).IDENTIFIER!=null?((FunctionContext)_localctx).IDENTIFIER.getText():null),_localctx.ret,((FunctionContext)_localctx).body.node)
			global_scope[(((FunctionContext)_localctx).IDENTIFIER!=null?((FunctionContext)_localctx).IDENTIFIER.getText():null)] = (_localctx.args,_localctx.ret)
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BodyContext extends ParserRuleContext {
		public  node;
		public  decl;
		public  stat;
		public DeclarationsContext declarations;
		public StatementsContext statements;
		public DeclarationsContext declarations() {
			return getRuleContext(DeclarationsContext.class,0);
		}
		public List<TerminalNode> NL() { return getTokens(GoParser.NL); }
		public TerminalNode NL(int i) {
			return getToken(GoParser.NL, i);
		}
		public StatementsContext statements() {
			return getRuleContext(StatementsContext.class,0);
		}
		public BodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body; }
	}

	public final BodyContext body() throws RecognitionException {
		BodyContext _localctx = new BodyContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_body);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(121);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VAR) {
				{
				setState(117);
				((BodyContext)_localctx).declarations = declarations();
				setState(118);
				match(NL);
				_localctx.decl = ((BodyContext)_localctx).declarations.node
				}
			}

			setState(126);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(123);
					match(NL);
					}
					} 
				}
				setState(128);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			}
			setState(132);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << RETURN) | (1L << IF) | (1L << FOR) | (1L << CLB) | (1L << IDENTIFIER))) != 0)) {
				{
				setState(129);
				((BodyContext)_localctx).statements = statements();
				_localctx.stat = ((BodyContext)_localctx).statements.node
				}
			}

			_localctx.node = self.bodyNode(_localctx.decl,_localctx.stat)

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Func_argsContext extends ParserRuleContext {
		public  args;
		public Token IDENTIFIER;
		public TypeContext type;
		public List<TerminalNode> IDENTIFIER() { return getTokens(GoParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(GoParser.IDENTIFIER, i);
		}
		public List<TypeContext> type() {
			return getRuleContexts(TypeContext.class);
		}
		public TypeContext type(int i) {
			return getRuleContext(TypeContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(GoParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(GoParser.COMMA, i);
		}
		public Func_argsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_args; }
	}

	public final Func_argsContext func_args() throws RecognitionException {
		Func_argsContext _localctx = new Func_argsContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_func_args);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(136);
			((Func_argsContext)_localctx).IDENTIFIER = match(IDENTIFIER);
			setState(137);
			((Func_argsContext)_localctx).type = type();
			_localctx.args = [((((Func_argsContext)_localctx).IDENTIFIER!=null?((Func_argsContext)_localctx).IDENTIFIER.getText():null),((Func_argsContext)_localctx).type.text)]
			setState(146);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(139);
				match(COMMA);
				setState(140);
				((Func_argsContext)_localctx).IDENTIFIER = match(IDENTIFIER);
				setState(141);
				((Func_argsContext)_localctx).type = type();
				_localctx.args.append(((((Func_argsContext)_localctx).IDENTIFIER!=null?((Func_argsContext)_localctx).IDENTIFIER.getText():null),((Func_argsContext)_localctx).type.text))
				}
				}
				setState(148);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypeContext extends ParserRuleContext {
		public  text;
		public TerminalNode INT_TYPE() { return getToken(GoParser.INT_TYPE, 0); }
		public TerminalNode BOOL_TYPE() { return getToken(GoParser.BOOL_TYPE, 0); }
		public TerminalNode FLOAT_TYPE() { return getToken(GoParser.FLOAT_TYPE, 0); }
		public TerminalNode STRING_TYPE() { return getToken(GoParser.STRING_TYPE, 0); }
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_type);
		try {
			setState(157);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT_TYPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(149);
				match(INT_TYPE);
				_localctx.text = 'INT'
				}
				break;
			case BOOL_TYPE:
				enterOuterAlt(_localctx, 2);
				{
				setState(151);
				match(BOOL_TYPE);
				_localctx.text = 'BOOL'
				}
				break;
			case FLOAT_TYPE:
				enterOuterAlt(_localctx, 3);
				{
				setState(153);
				match(FLOAT_TYPE);
				_localctx.text = 'FLOAT'
				}
				break;
			case STRING_TYPE:
				enterOuterAlt(_localctx, 4);
				{
				setState(155);
				match(STRING_TYPE);
				_localctx.text = 'STRING'
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclarationsContext extends ParserRuleContext {
		public  node;
		public DeclarationContext declaration;
		public DeclarationsContext declarations;
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public TerminalNode NL() { return getToken(GoParser.NL, 0); }
		public DeclarationsContext declarations() {
			return getRuleContext(DeclarationsContext.class,0);
		}
		public DeclarationsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declarations; }
	}

	public final DeclarationsContext declarations() throws RecognitionException {
		DeclarationsContext _localctx = new DeclarationsContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_declarations);
		try {
			setState(167);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(159);
				((DeclarationsContext)_localctx).declaration = declaration();
				setState(160);
				match(NL);
				setState(161);
				((DeclarationsContext)_localctx).declarations = declarations();
				_localctx.node = self.blockNode(((DeclarationsContext)_localctx).declaration.node, ((DeclarationsContext)_localctx).declarations.node, 'DECL')

				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(164);
				((DeclarationsContext)_localctx).declaration = declaration();
				_localctx.node = self.blockNode(((DeclarationsContext)_localctx).declaration.node, None, 'DECL')
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclarationContext extends ParserRuleContext {
		public  node;
		public Token IDENTIFIER;
		public TypeContext type;
		public ExprContext expr;
		public TerminalNode VAR() { return getToken(GoParser.VAR, 0); }
		public TerminalNode IDENTIFIER() { return getToken(GoParser.IDENTIFIER, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(GoParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(169);
			match(VAR);
			setState(170);
			((DeclarationContext)_localctx).IDENTIFIER = match(IDENTIFIER);
			setState(171);
			((DeclarationContext)_localctx).type = type();
			setState(172);
			match(ASSIGN);
			setState(173);
			((DeclarationContext)_localctx).expr = expr(0);
			_localctx.node = self.declNode((((DeclarationContext)_localctx).IDENTIFIER!=null?((DeclarationContext)_localctx).IDENTIFIER.getText():null), ((DeclarationContext)_localctx).type.text, ((DeclarationContext)_localctx).expr.node)
					
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementsContext extends ParserRuleContext {
		public  node;
		public StatementContext statement;
		public StatementsContext statements;
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public TerminalNode NL() { return getToken(GoParser.NL, 0); }
		public StatementsContext statements() {
			return getRuleContext(StatementsContext.class,0);
		}
		public StatementsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statements; }
	}

	public final StatementsContext statements() throws RecognitionException {
		StatementsContext _localctx = new StatementsContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_statements);
		try {
			setState(184);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(176);
				((StatementsContext)_localctx).statement = statement();
				setState(177);
				match(NL);
				setState(178);
				((StatementsContext)_localctx).statements = statements();
				_localctx.node = self.blockNode(((StatementsContext)_localctx).statement.node, ((StatementsContext)_localctx).statements.node, 'STMT')
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(181);
				((StatementsContext)_localctx).statement = statement();
				_localctx.node = self.blockNode(((StatementsContext)_localctx).statement.node, None, 'STMT')
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public  node;
		public AssignmentContext assignment;
		public Block_stmtContext block_stmt;
		public If_controlContext if_control;
		public For_loopContext for_loop;
		public Func_callContext func_call;
		public ExprContext expr;
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public Block_stmtContext block_stmt() {
			return getRuleContext(Block_stmtContext.class,0);
		}
		public If_controlContext if_control() {
			return getRuleContext(If_controlContext.class,0);
		}
		public For_loopContext for_loop() {
			return getRuleContext(For_loopContext.class,0);
		}
		public Func_callContext func_call() {
			return getRuleContext(Func_callContext.class,0);
		}
		public TerminalNode RETURN() { return getToken(GoParser.RETURN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_statement);
		int _la;
		try {
			setState(208);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(186);
				((StatementContext)_localctx).assignment = assignment();
				_localctx.node = ((StatementContext)_localctx).assignment.node
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(189);
				((StatementContext)_localctx).block_stmt = block_stmt();
				_localctx.node = ((StatementContext)_localctx).block_stmt.node
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(192);
				((StatementContext)_localctx).if_control = if_control();
				_localctx.node = ((StatementContext)_localctx).if_control.node
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(195);
				((StatementContext)_localctx).for_loop = for_loop();
				_localctx.node = ((StatementContext)_localctx).for_loop.node
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(198);
				((StatementContext)_localctx).func_call = func_call();
				_localctx.node = ((StatementContext)_localctx).func_call.node
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(201);
				match(RETURN);
				setState(205);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PLUS) | (1L << MINUS) | (1L << NOT) | (1L << INTEGER) | (1L << FLOAT) | (1L << BOOL) | (1L << STRING) | (1L << LB) | (1L << IDENTIFIER))) != 0)) {
					{
					setState(202);
					((StatementContext)_localctx).expr = expr(0);
					_localctx.node= ((StatementContext)_localctx).expr.node
					}
				}

				_localctx.node = self.returnNode(_localctx.node)
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Block_stmtContext extends ParserRuleContext {
		public  node;
		public StatementsContext statements;
		public TerminalNode CLB() { return getToken(GoParser.CLB, 0); }
		public TerminalNode CRB() { return getToken(GoParser.CRB, 0); }
		public List<TerminalNode> NL() { return getTokens(GoParser.NL); }
		public TerminalNode NL(int i) {
			return getToken(GoParser.NL, i);
		}
		public StatementsContext statements() {
			return getRuleContext(StatementsContext.class,0);
		}
		public Block_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block_stmt; }
	}

	public final Block_stmtContext block_stmt() throws RecognitionException {
		Block_stmtContext _localctx = new Block_stmtContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_block_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(210);
			match(CLB);
			setState(212);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				{
				setState(211);
				match(NL);
				}
				break;
			}
			setState(215);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << RETURN) | (1L << IF) | (1L << FOR) | (1L << CLB) | (1L << IDENTIFIER))) != 0)) {
				{
				setState(214);
				((Block_stmtContext)_localctx).statements = statements();
				}
			}

			setState(218);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(217);
				match(NL);
				}
			}

			setState(220);
			match(CRB);
			_localctx.node = ((Block_stmtContext)_localctx).statements.node
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignmentContext extends ParserRuleContext {
		public  node;
		public Token IDENTIFIER;
		public ExprContext expr;
		public TerminalNode IDENTIFIER() { return getToken(GoParser.IDENTIFIER, 0); }
		public TerminalNode ASSIGN() { return getToken(GoParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(223);
			((AssignmentContext)_localctx).IDENTIFIER = match(IDENTIFIER);
			setState(224);
			match(ASSIGN);
			setState(225);
			((AssignmentContext)_localctx).expr = expr(0);
			_localctx.node = self.assignNode((((AssignmentContext)_localctx).IDENTIFIER!=null?((AssignmentContext)_localctx).IDENTIFIER.getText():null), ((AssignmentContext)_localctx).expr.node)
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_controlContext extends ParserRuleContext {
		public  node;
		public  stat1;
		public  stat2;
		public ExprContext expr;
		public StatementsContext statements;
		public TerminalNode IF() { return getToken(GoParser.IF, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public List<TerminalNode> CLB() { return getTokens(GoParser.CLB); }
		public TerminalNode CLB(int i) {
			return getToken(GoParser.CLB, i);
		}
		public List<TerminalNode> CRB() { return getTokens(GoParser.CRB); }
		public TerminalNode CRB(int i) {
			return getToken(GoParser.CRB, i);
		}
		public TerminalNode ELSE() { return getToken(GoParser.ELSE, 0); }
		public List<TerminalNode> NL() { return getTokens(GoParser.NL); }
		public TerminalNode NL(int i) {
			return getToken(GoParser.NL, i);
		}
		public List<StatementsContext> statements() {
			return getRuleContexts(StatementsContext.class);
		}
		public StatementsContext statements(int i) {
			return getRuleContext(StatementsContext.class,i);
		}
		public If_controlContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_control; }
	}

	public final If_controlContext if_control() throws RecognitionException {
		If_controlContext _localctx = new If_controlContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_if_control);
		int _la;
		try {
			setState(288);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,37,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(228);
				match(IF);
				setState(229);
				((If_controlContext)_localctx).expr = expr(0);
				setState(231);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NL) {
					{
					setState(230);
					match(NL);
					}
				}

				setState(233);
				match(CLB);
				setState(235);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
				case 1:
					{
					setState(234);
					match(NL);
					}
					break;
				}
				setState(240);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << RETURN) | (1L << IF) | (1L << FOR) | (1L << CLB) | (1L << IDENTIFIER))) != 0)) {
					{
					setState(237);
					((If_controlContext)_localctx).statements = statements();
					_localctx.stat1= ((If_controlContext)_localctx).statements.node
					}
				}

				setState(243);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NL) {
					{
					setState(242);
					match(NL);
					}
				}

				setState(245);
				match(CRB);
				setState(247);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NL) {
					{
					setState(246);
					match(NL);
					}
				}

				setState(249);
				match(ELSE);
				setState(251);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NL) {
					{
					setState(250);
					match(NL);
					}
				}

				setState(253);
				match(CLB);
				setState(255);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
				case 1:
					{
					setState(254);
					match(NL);
					}
					break;
				}
				setState(260);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << RETURN) | (1L << IF) | (1L << FOR) | (1L << CLB) | (1L << IDENTIFIER))) != 0)) {
					{
					setState(257);
					((If_controlContext)_localctx).statements = statements();
					_localctx.stat2 = ((If_controlContext)_localctx).statements.node
					}
				}

				setState(263);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NL) {
					{
					setState(262);
					match(NL);
					}
				}

				setState(265);
				match(CRB);
				_localctx.node= self.ifNode(((If_controlContext)_localctx).expr.node, _localctx.stat1, _localctx.stat2)
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(268);
				match(IF);
				setState(269);
				((If_controlContext)_localctx).expr = expr(0);
				setState(271);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NL) {
					{
					setState(270);
					match(NL);
					}
				}

				setState(273);
				match(CLB);
				setState(275);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,34,_ctx) ) {
				case 1:
					{
					setState(274);
					match(NL);
					}
					break;
				}
				setState(280);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << RETURN) | (1L << IF) | (1L << FOR) | (1L << CLB) | (1L << IDENTIFIER))) != 0)) {
					{
					setState(277);
					((If_controlContext)_localctx).statements = statements();
					_localctx.stat1= ((If_controlContext)_localctx).statements.node
					}
				}

				setState(283);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NL) {
					{
					setState(282);
					match(NL);
					}
				}

				setState(285);
				match(CRB);
				_localctx.node= self.ifNode(((If_controlContext)_localctx).expr.node, _localctx.stat1)

				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class For_loopContext extends ParserRuleContext {
		public  node;
		public  stat;
		public ExprContext expr;
		public StatementsContext statements;
		public TerminalNode FOR() { return getToken(GoParser.FOR, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode CLB() { return getToken(GoParser.CLB, 0); }
		public TerminalNode CRB() { return getToken(GoParser.CRB, 0); }
		public List<TerminalNode> NL() { return getTokens(GoParser.NL); }
		public TerminalNode NL(int i) {
			return getToken(GoParser.NL, i);
		}
		public StatementsContext statements() {
			return getRuleContext(StatementsContext.class,0);
		}
		public For_loopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_loop; }
	}

	public final For_loopContext for_loop() throws RecognitionException {
		For_loopContext _localctx = new For_loopContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_for_loop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(290);
			match(FOR);
			setState(291);
			((For_loopContext)_localctx).expr = expr(0);
			setState(293);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(292);
				match(NL);
				}
			}

			setState(295);
			match(CLB);
			setState(297);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,39,_ctx) ) {
			case 1:
				{
				setState(296);
				match(NL);
				}
				break;
			}
			setState(302);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << RETURN) | (1L << IF) | (1L << FOR) | (1L << CLB) | (1L << IDENTIFIER))) != 0)) {
				{
				setState(299);
				((For_loopContext)_localctx).statements = statements();
				_localctx.stat = ((For_loopContext)_localctx).statements.node
				}
			}

			setState(305);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(304);
				match(NL);
				}
			}

			setState(307);
			match(CRB);
			_localctx.node = self.forNode(((For_loopContext)_localctx).expr.node, _localctx.stat)
					
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Func_callContext extends ParserRuleContext {
		public  node;
		public  id;
		public  args;
		public Token IDENTIFIER;
		public ExprContext expr;
		public List<TerminalNode> IDENTIFIER() { return getTokens(GoParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(GoParser.IDENTIFIER, i);
		}
		public TerminalNode LB() { return getToken(GoParser.LB, 0); }
		public TerminalNode RB() { return getToken(GoParser.RB, 0); }
		public List<TerminalNode> DOT() { return getTokens(GoParser.DOT); }
		public TerminalNode DOT(int i) {
			return getToken(GoParser.DOT, i);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(GoParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(GoParser.COMMA, i);
		}
		public Func_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_call; }
	}

	public final Func_callContext func_call() throws RecognitionException {
		Func_callContext _localctx = new Func_callContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_func_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(310);
			((Func_callContext)_localctx).IDENTIFIER = match(IDENTIFIER);
			_localctx.id = (((Func_callContext)_localctx).IDENTIFIER!=null?((Func_callContext)_localctx).IDENTIFIER.getText():null)
			setState(317);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DOT) {
				{
				{
				setState(312);
				match(DOT);
				setState(313);
				((Func_callContext)_localctx).IDENTIFIER = match(IDENTIFIER);
				_localctx.id += "." + (((Func_callContext)_localctx).IDENTIFIER!=null?((Func_callContext)_localctx).IDENTIFIER.getText():null)
				}
				}
				setState(319);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(320);
			match(LB);
			setState(332);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PLUS) | (1L << MINUS) | (1L << NOT) | (1L << INTEGER) | (1L << FLOAT) | (1L << BOOL) | (1L << STRING) | (1L << LB) | (1L << IDENTIFIER))) != 0)) {
				{
				setState(321);
				((Func_callContext)_localctx).expr = expr(0);
				_localctx.args = [((Func_callContext)_localctx).expr.node]
				setState(329);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(323);
					match(COMMA);
					setState(324);
					((Func_callContext)_localctx).expr = expr(0);
					_localctx.args.append(((Func_callContext)_localctx).expr.node)
					}
					}
					setState(331);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(334);
			match(RB);
			_localctx.node=self.funcCallNode(_localctx.id,_localctx.args)
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public  node;
		public ExprContext left;
		public Token IDENTIFIER;
		public Func_callContext func_call;
		public LiteralsContext literals;
		public ExprContext expr;
		public Token op;
		public ExprContext right;
		public TerminalNode IDENTIFIER() { return getToken(GoParser.IDENTIFIER, 0); }
		public Func_callContext func_call() {
			return getRuleContext(Func_callContext.class,0);
		}
		public LiteralsContext literals() {
			return getRuleContext(LiteralsContext.class,0);
		}
		public TerminalNode LB() { return getToken(GoParser.LB, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode RB() { return getToken(GoParser.RB, 0); }
		public TerminalNode NOT() { return getToken(GoParser.NOT, 0); }
		public TerminalNode PLUS() { return getToken(GoParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(GoParser.MINUS, 0); }
		public TerminalNode STAR() { return getToken(GoParser.STAR, 0); }
		public TerminalNode DIVISON() { return getToken(GoParser.DIVISON, 0); }
		public TerminalNode MODULO() { return getToken(GoParser.MODULO, 0); }
		public TerminalNode UNEQUAL() { return getToken(GoParser.UNEQUAL, 0); }
		public TerminalNode EQUALS() { return getToken(GoParser.EQUALS, 0); }
		public TerminalNode LESS() { return getToken(GoParser.LESS, 0); }
		public TerminalNode GREATER() { return getToken(GoParser.GREATER, 0); }
		public TerminalNode LESSEQUAL() { return getToken(GoParser.LESSEQUAL, 0); }
		public TerminalNode GREATEREQUAL() { return getToken(GoParser.GREATEREQUAL, 0); }
		public TerminalNode OR() { return getToken(GoParser.OR, 0); }
		public TerminalNode AND() { return getToken(GoParser.AND, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 32;
		enterRecursionRule(_localctx, 32, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(355);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,45,_ctx) ) {
			case 1:
				{
				setState(338);
				((ExprContext)_localctx).IDENTIFIER = match(IDENTIFIER);
				_localctx.node= self.idNode((((ExprContext)_localctx).IDENTIFIER!=null?((ExprContext)_localctx).IDENTIFIER.getText():null),None)
				}
				break;
			case 2:
				{
				setState(340);
				((ExprContext)_localctx).func_call = func_call();
				_localctx.node = ((ExprContext)_localctx).func_call.node
				}
				break;
			case 3:
				{
				setState(343);
				((ExprContext)_localctx).literals = literals();
				_localctx.node = ((ExprContext)_localctx).literals.node
				}
				break;
			case 4:
				{
				setState(346);
				match(LB);
				setState(347);
				((ExprContext)_localctx).expr = expr(0);
				setState(348);
				match(RB);
				_localctx.node = ((ExprContext)_localctx).expr.node
				}
				break;
			case 5:
				{
				setState(351);
				((ExprContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PLUS) | (1L << MINUS) | (1L << NOT))) != 0)) ) {
					((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(352);
				((ExprContext)_localctx).expr = expr(5);
				_localctx.node = self.unaryNode((((ExprContext)_localctx).op!=null?((ExprContext)_localctx).op.getText():null), ((ExprContext)_localctx).expr.node)
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(379);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,47,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(377);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,46,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						_localctx.left = _prevctx;
						_localctx.left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(357);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(358);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << STAR) | (1L << DIVISON) | (1L << MODULO))) != 0)) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(359);
						((ExprContext)_localctx).right = ((ExprContext)_localctx).expr = expr(5);
						_localctx.node = self.binaryNode(((ExprContext)_localctx).left.node, (((ExprContext)_localctx).op!=null?((ExprContext)_localctx).op.getText():null), ((ExprContext)_localctx).right.node)
						          		
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						_localctx.left = _prevctx;
						_localctx.left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(362);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(363);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==PLUS || _la==MINUS) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(364);
						((ExprContext)_localctx).right = ((ExprContext)_localctx).expr = expr(4);
						_localctx.node = self.binaryNode(((ExprContext)_localctx).left.node, (((ExprContext)_localctx).op!=null?((ExprContext)_localctx).op.getText():null), ((ExprContext)_localctx).right.node)
						          		
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						_localctx.left = _prevctx;
						_localctx.left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(367);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(368);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQUALS) | (1L << UNEQUAL) | (1L << LESS) | (1L << GREATER) | (1L << LESSEQUAL) | (1L << GREATEREQUAL))) != 0)) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(369);
						((ExprContext)_localctx).right = ((ExprContext)_localctx).expr = expr(3);
						_localctx.node = self.binaryNode(((ExprContext)_localctx).left.node, (((ExprContext)_localctx).op!=null?((ExprContext)_localctx).op.getText():null), ((ExprContext)_localctx).right.node)
						          		
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						_localctx.left = _prevctx;
						_localctx.left = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(372);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(373);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==AND || _la==OR) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(374);
						((ExprContext)_localctx).right = ((ExprContext)_localctx).expr = expr(2);
						_localctx.node = self.binaryNode(((ExprContext)_localctx).left.node, (((ExprContext)_localctx).op!=null?((ExprContext)_localctx).op.getText():null), ((ExprContext)_localctx).right.node)
						          		
						}
						break;
					}
					} 
				}
				setState(381);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,47,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class LiteralsContext extends ParserRuleContext {
		public  node;
		public Token INTEGER;
		public Token STRING;
		public Token FLOAT;
		public Token BOOL;
		public TerminalNode INTEGER() { return getToken(GoParser.INTEGER, 0); }
		public TerminalNode STRING() { return getToken(GoParser.STRING, 0); }
		public TerminalNode FLOAT() { return getToken(GoParser.FLOAT, 0); }
		public TerminalNode BOOL() { return getToken(GoParser.BOOL, 0); }
		public LiteralsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literals; }
	}

	public final LiteralsContext literals() throws RecognitionException {
		LiteralsContext _localctx = new LiteralsContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_literals);
		try {
			setState(390);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTEGER:
				enterOuterAlt(_localctx, 1);
				{
				setState(382);
				((LiteralsContext)_localctx).INTEGER = match(INTEGER);
				_localctx.node =self.atomNode((((LiteralsContext)_localctx).INTEGER!=null?((LiteralsContext)_localctx).INTEGER.getText():null),'INT')
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(384);
				((LiteralsContext)_localctx).STRING = match(STRING);
				_localctx.node = self.atomNode((((LiteralsContext)_localctx).STRING!=null?((LiteralsContext)_localctx).STRING.getText():null),'STRING')
				}
				break;
			case FLOAT:
				enterOuterAlt(_localctx, 3);
				{
				setState(386);
				((LiteralsContext)_localctx).FLOAT = match(FLOAT);
				_localctx.node = self.atomNode((((LiteralsContext)_localctx).FLOAT!=null?((LiteralsContext)_localctx).FLOAT.getText():null), 'FLOAT')
				}
				break;
			case BOOL:
				enterOuterAlt(_localctx, 4);
				{
				setState(388);
				((LiteralsContext)_localctx).BOOL = match(BOOL);
				_localctx.node = self.atomNode((((LiteralsContext)_localctx).BOOL!=null?((LiteralsContext)_localctx).BOOL.getText():null), 'BOOL')
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 0:
			return program_sempred((ProgramContext)_localctx, predIndex);
		case 1:
			return main_function_sempred((Main_functionContext)_localctx, predIndex);
		case 16:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean program_sempred(ProgramContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return (((ProgramContext)_localctx).IDENTIFIER!=null?((ProgramContext)_localctx).IDENTIFIER.getText():null) == "main" ;
		}
		return true;
	}
	private boolean main_function_sempred(Main_functionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return (((Main_functionContext)_localctx).IDENTIFIER!=null?((Main_functionContext)_localctx).IDENTIFIER.getText():null) == "main" ;
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 4);
		case 3:
			return precpred(_ctx, 3);
		case 4:
			return precpred(_ctx, 2);
		case 5:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3,\u018b\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\3\2\3\2\3\2\3\2\3\2\3\2\7\2-\n\2\f\2\16\2\60\13\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\5\28\n\2\3\2\5\2;\n\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\5\3F\n\3\3\3\3\3\5\3J\n\3\3\3\3\3\5\3N\n\3\3\3\3\3\3\3\3\4\3\4\3\4"+
		"\3\4\3\4\5\4X\n\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5b\n\5\3\5\3\5\3\5"+
		"\3\5\5\5h\n\5\3\5\5\5k\n\5\3\5\3\5\5\5o\n\5\3\5\3\5\5\5s\n\5\3\5\3\5\3"+
		"\5\3\6\3\6\3\6\3\6\5\6|\n\6\3\6\7\6\177\n\6\f\6\16\6\u0082\13\6\3\6\3"+
		"\6\3\6\5\6\u0087\n\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u0093"+
		"\n\7\f\7\16\7\u0096\13\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00a0\n\b"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00aa\n\t\3\n\3\n\3\n\3\n\3\n\3\n"+
		"\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00bb\n\13\3\f\3\f\3"+
		"\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f"+
		"\u00d0\n\f\3\f\5\f\u00d3\n\f\3\r\3\r\5\r\u00d7\n\r\3\r\5\r\u00da\n\r\3"+
		"\r\5\r\u00dd\n\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\5"+
		"\17\u00ea\n\17\3\17\3\17\5\17\u00ee\n\17\3\17\3\17\3\17\5\17\u00f3\n\17"+
		"\3\17\5\17\u00f6\n\17\3\17\3\17\5\17\u00fa\n\17\3\17\3\17\5\17\u00fe\n"+
		"\17\3\17\3\17\5\17\u0102\n\17\3\17\3\17\3\17\5\17\u0107\n\17\3\17\5\17"+
		"\u010a\n\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u0112\n\17\3\17\3\17\5"+
		"\17\u0116\n\17\3\17\3\17\3\17\5\17\u011b\n\17\3\17\5\17\u011e\n\17\3\17"+
		"\3\17\3\17\5\17\u0123\n\17\3\20\3\20\3\20\5\20\u0128\n\20\3\20\3\20\5"+
		"\20\u012c\n\20\3\20\3\20\3\20\5\20\u0131\n\20\3\20\5\20\u0134\n\20\3\20"+
		"\3\20\3\20\3\21\3\21\3\21\3\21\3\21\7\21\u013e\n\21\f\21\16\21\u0141\13"+
		"\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u014a\n\21\f\21\16\21\u014d"+
		"\13\21\5\21\u014f\n\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3"+
		"\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u0166"+
		"\n\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22"+
		"\3\22\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u017c\n\22\f\22\16\22\u017f\13"+
		"\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0189\n\23\3\23\2\3\""+
		"\24\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$\2\7\4\2\17\20\34\34\3\2"+
		"\21\23\3\2\17\20\3\2\24\31\3\2\32\33\2\u01b6\2&\3\2\2\2\4?\3\2\2\2\6R"+
		"\3\2\2\2\b[\3\2\2\2\n{\3\2\2\2\f\u008a\3\2\2\2\16\u009f\3\2\2\2\20\u00a9"+
		"\3\2\2\2\22\u00ab\3\2\2\2\24\u00ba\3\2\2\2\26\u00d2\3\2\2\2\30\u00d4\3"+
		"\2\2\2\32\u00e1\3\2\2\2\34\u0122\3\2\2\2\36\u0124\3\2\2\2 \u0138\3\2\2"+
		"\2\"\u0165\3\2\2\2$\u0188\3\2\2\2&\'\7\6\2\2\'(\7,\2\2()\6\2\2\3).\7!"+
		"\2\2*+\7\7\2\2+-\7 \2\2,*\3\2\2\2-\60\3\2\2\2.,\3\2\2\2./\3\2\2\2/\61"+
		"\3\2\2\2\60.\3\2\2\2\61\62\7!\2\2\62\67\5\4\3\2\63\64\7!\2\2\64\65\5\6"+
		"\4\2\65\66\b\2\1\2\668\3\2\2\2\67\63\3\2\2\2\678\3\2\2\28:\3\2\2\29;\7"+
		"!\2\2:9\3\2\2\2:;\3\2\2\2;<\3\2\2\2<=\7\2\2\3=>\b\2\1\2>\3\3\2\2\2?@\7"+
		"\5\2\2@A\7,\2\2AB\6\3\3\3BC\7\"\2\2CE\7#\2\2DF\7!\2\2ED\3\2\2\2EF\3\2"+
		"\2\2FG\3\2\2\2GI\7$\2\2HJ\7!\2\2IH\3\2\2\2IJ\3\2\2\2JK\3\2\2\2KM\5\n\6"+
		"\2LN\7!\2\2ML\3\2\2\2MN\3\2\2\2NO\3\2\2\2OP\7%\2\2PQ\b\3\1\2Q\5\3\2\2"+
		"\2RW\5\b\5\2ST\7!\2\2TU\5\6\4\2UV\b\4\1\2VX\3\2\2\2WS\3\2\2\2WX\3\2\2"+
		"\2XY\3\2\2\2YZ\b\4\1\2Z\7\3\2\2\2[\\\7\5\2\2\\]\7,\2\2]a\7\"\2\2^_\5\f"+
		"\7\2_`\b\5\1\2`b\3\2\2\2a^\3\2\2\2ab\3\2\2\2bc\3\2\2\2cg\7#\2\2de\5\16"+
		"\b\2ef\b\5\1\2fh\3\2\2\2gd\3\2\2\2gh\3\2\2\2hj\3\2\2\2ik\7!\2\2ji\3\2"+
		"\2\2jk\3\2\2\2kl\3\2\2\2ln\7$\2\2mo\7!\2\2nm\3\2\2\2no\3\2\2\2op\3\2\2"+
		"\2pr\5\n\6\2qs\7!\2\2rq\3\2\2\2rs\3\2\2\2st\3\2\2\2tu\7%\2\2uv\b\5\1\2"+
		"v\t\3\2\2\2wx\5\20\t\2xy\7!\2\2yz\b\6\1\2z|\3\2\2\2{w\3\2\2\2{|\3\2\2"+
		"\2|\u0080\3\2\2\2}\177\7!\2\2~}\3\2\2\2\177\u0082\3\2\2\2\u0080~\3\2\2"+
		"\2\u0080\u0081\3\2\2\2\u0081\u0086\3\2\2\2\u0082\u0080\3\2\2\2\u0083\u0084"+
		"\5\24\13\2\u0084\u0085\b\6\1\2\u0085\u0087\3\2\2\2\u0086\u0083\3\2\2\2"+
		"\u0086\u0087\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089\b\6\1\2\u0089\13"+
		"\3\2\2\2\u008a\u008b\7,\2\2\u008b\u008c\5\16\b\2\u008c\u0094\b\7\1\2\u008d"+
		"\u008e\7&\2\2\u008e\u008f\7,\2\2\u008f\u0090\5\16\b\2\u0090\u0091\b\7"+
		"\1\2\u0091\u0093\3\2\2\2\u0092\u008d\3\2\2\2\u0093\u0096\3\2\2\2\u0094"+
		"\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\r\3\2\2\2\u0096\u0094\3\2\2\2"+
		"\u0097\u0098\7\13\2\2\u0098\u00a0\b\b\1\2\u0099\u009a\7\r\2\2\u009a\u00a0"+
		"\b\b\1\2\u009b\u009c\7\f\2\2\u009c\u00a0\b\b\1\2\u009d\u009e\7\16\2\2"+
		"\u009e\u00a0\b\b\1\2\u009f\u0097\3\2\2\2\u009f\u0099\3\2\2\2\u009f\u009b"+
		"\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\17\3\2\2\2\u00a1\u00a2\5\22\n\2\u00a2"+
		"\u00a3\7!\2\2\u00a3\u00a4\5\20\t\2\u00a4\u00a5\b\t\1\2\u00a5\u00aa\3\2"+
		"\2\2\u00a6\u00a7\5\22\n\2\u00a7\u00a8\b\t\1\2\u00a8\u00aa\3\2\2\2\u00a9"+
		"\u00a1\3\2\2\2\u00a9\u00a6\3\2\2\2\u00aa\21\3\2\2\2\u00ab\u00ac\7\3\2"+
		"\2\u00ac\u00ad\7,\2\2\u00ad\u00ae\5\16\b\2\u00ae\u00af\7)\2\2\u00af\u00b0"+
		"\5\"\22\2\u00b0\u00b1\b\n\1\2\u00b1\23\3\2\2\2\u00b2\u00b3\5\26\f\2\u00b3"+
		"\u00b4\7!\2\2\u00b4\u00b5\5\24\13\2\u00b5\u00b6\b\13\1\2\u00b6\u00bb\3"+
		"\2\2\2\u00b7\u00b8\5\26\f\2\u00b8\u00b9\b\13\1\2\u00b9\u00bb\3\2\2\2\u00ba"+
		"\u00b2\3\2\2\2\u00ba\u00b7\3\2\2\2\u00bb\25\3\2\2\2\u00bc\u00bd\5\32\16"+
		"\2\u00bd\u00be\b\f\1\2\u00be\u00d3\3\2\2\2\u00bf\u00c0\5\30\r\2\u00c0"+
		"\u00c1\b\f\1\2\u00c1\u00d3\3\2\2\2\u00c2\u00c3\5\34\17\2\u00c3\u00c4\b"+
		"\f\1\2\u00c4\u00d3\3\2\2\2\u00c5\u00c6\5\36\20\2\u00c6\u00c7\b\f\1\2\u00c7"+
		"\u00d3\3\2\2\2\u00c8\u00c9\5 \21\2\u00c9\u00ca\b\f\1\2\u00ca\u00d3\3\2"+
		"\2\2\u00cb\u00cf\7\4\2\2\u00cc\u00cd\5\"\22\2\u00cd\u00ce\b\f\1\2\u00ce"+
		"\u00d0\3\2\2\2\u00cf\u00cc\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1\3\2"+
		"\2\2\u00d1\u00d3\b\f\1\2\u00d2\u00bc\3\2\2\2\u00d2\u00bf\3\2\2\2\u00d2"+
		"\u00c2\3\2\2\2\u00d2\u00c5\3\2\2\2\u00d2\u00c8\3\2\2\2\u00d2\u00cb\3\2"+
		"\2\2\u00d3\27\3\2\2\2\u00d4\u00d6\7$\2\2\u00d5\u00d7\7!\2\2\u00d6\u00d5"+
		"\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d9\3\2\2\2\u00d8\u00da\5\24\13\2"+
		"\u00d9\u00d8\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00dc\3\2\2\2\u00db\u00dd"+
		"\7!\2\2\u00dc\u00db\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de\3\2\2\2\u00de"+
		"\u00df\7%\2\2\u00df\u00e0\b\r\1\2\u00e0\31\3\2\2\2\u00e1\u00e2\7,\2\2"+
		"\u00e2\u00e3\7)\2\2\u00e3\u00e4\5\"\22\2\u00e4\u00e5\b\16\1\2\u00e5\33"+
		"\3\2\2\2\u00e6\u00e7\7\b\2\2\u00e7\u00e9\5\"\22\2\u00e8\u00ea\7!\2\2\u00e9"+
		"\u00e8\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ed\7$"+
		"\2\2\u00ec\u00ee\7!\2\2\u00ed\u00ec\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee"+
		"\u00f2\3\2\2\2\u00ef\u00f0\5\24\13\2\u00f0\u00f1\b\17\1\2\u00f1\u00f3"+
		"\3\2\2\2\u00f2\u00ef\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f5\3\2\2\2\u00f4"+
		"\u00f6\7!\2\2\u00f5\u00f4\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7\3\2"+
		"\2\2\u00f7\u00f9\7%\2\2\u00f8\u00fa\7!\2\2\u00f9\u00f8\3\2\2\2\u00f9\u00fa"+
		"\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00fd\7\t\2\2\u00fc\u00fe\7!\2\2\u00fd"+
		"\u00fc\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0101\7$"+
		"\2\2\u0100\u0102\7!\2\2\u0101\u0100\3\2\2\2\u0101\u0102\3\2\2\2\u0102"+
		"\u0106\3\2\2\2\u0103\u0104\5\24\13\2\u0104\u0105\b\17\1\2\u0105\u0107"+
		"\3\2\2\2\u0106\u0103\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0109\3\2\2\2\u0108"+
		"\u010a\7!\2\2\u0109\u0108\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010b\3\2"+
		"\2\2\u010b\u010c\7%\2\2\u010c\u010d\b\17\1\2\u010d\u0123\3\2\2\2\u010e"+
		"\u010f\7\b\2\2\u010f\u0111\5\"\22\2\u0110\u0112\7!\2\2\u0111\u0110\3\2"+
		"\2\2\u0111\u0112\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0115\7$\2\2\u0114"+
		"\u0116\7!\2\2\u0115\u0114\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u011a\3\2"+
		"\2\2\u0117\u0118\5\24\13\2\u0118\u0119\b\17\1\2\u0119\u011b\3\2\2\2\u011a"+
		"\u0117\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011d\3\2\2\2\u011c\u011e\7!"+
		"\2\2\u011d\u011c\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u011f\3\2\2\2\u011f"+
		"\u0120\7%\2\2\u0120\u0121\b\17\1\2\u0121\u0123\3\2\2\2\u0122\u00e6\3\2"+
		"\2\2\u0122\u010e\3\2\2\2\u0123\35\3\2\2\2\u0124\u0125\7\n\2\2\u0125\u0127"+
		"\5\"\22\2\u0126\u0128\7!\2\2\u0127\u0126\3\2\2\2\u0127\u0128\3\2\2\2\u0128"+
		"\u0129\3\2\2\2\u0129\u012b\7$\2\2\u012a\u012c\7!\2\2\u012b\u012a\3\2\2"+
		"\2\u012b\u012c\3\2\2\2\u012c\u0130\3\2\2\2\u012d\u012e\5\24\13\2\u012e"+
		"\u012f\b\20\1\2\u012f\u0131\3\2\2\2\u0130\u012d\3\2\2\2\u0130\u0131\3"+
		"\2\2\2\u0131\u0133\3\2\2\2\u0132\u0134\7!\2\2\u0133\u0132\3\2\2\2\u0133"+
		"\u0134\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136\7%\2\2\u0136\u0137\b\20"+
		"\1\2\u0137\37\3\2\2\2\u0138\u0139\7,\2\2\u0139\u013f\b\21\1\2\u013a\u013b"+
		"\7\'\2\2\u013b\u013c\7,\2\2\u013c\u013e\b\21\1\2\u013d\u013a\3\2\2\2\u013e"+
		"\u0141\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0142\3\2"+
		"\2\2\u0141\u013f\3\2\2\2\u0142\u014e\7\"\2\2\u0143\u0144\5\"\22\2\u0144"+
		"\u014b\b\21\1\2\u0145\u0146\7&\2\2\u0146\u0147\5\"\22\2\u0147\u0148\b"+
		"\21\1\2\u0148\u014a\3\2\2\2\u0149\u0145\3\2\2\2\u014a\u014d\3\2\2\2\u014b"+
		"\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014f\3\2\2\2\u014d\u014b\3\2"+
		"\2\2\u014e\u0143\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0150\3\2\2\2\u0150"+
		"\u0151\7#\2\2\u0151\u0152\b\21\1\2\u0152!\3\2\2\2\u0153\u0154\b\22\1\2"+
		"\u0154\u0155\7,\2\2\u0155\u0166\b\22\1\2\u0156\u0157\5 \21\2\u0157\u0158"+
		"\b\22\1\2\u0158\u0166\3\2\2\2\u0159\u015a\5$\23\2\u015a\u015b\b\22\1\2"+
		"\u015b\u0166\3\2\2\2\u015c\u015d\7\"\2\2\u015d\u015e\5\"\22\2\u015e\u015f"+
		"\7#\2\2\u015f\u0160\b\22\1\2\u0160\u0166\3\2\2\2\u0161\u0162\t\2\2\2\u0162"+
		"\u0163\5\"\22\7\u0163\u0164\b\22\1\2\u0164\u0166\3\2\2\2\u0165\u0153\3"+
		"\2\2\2\u0165\u0156\3\2\2\2\u0165\u0159\3\2\2\2\u0165\u015c\3\2\2\2\u0165"+
		"\u0161\3\2\2\2\u0166\u017d\3\2\2\2\u0167\u0168\f\6\2\2\u0168\u0169\t\3"+
		"\2\2\u0169\u016a\5\"\22\7\u016a\u016b\b\22\1\2\u016b\u017c\3\2\2\2\u016c"+
		"\u016d\f\5\2\2\u016d\u016e\t\4\2\2\u016e\u016f\5\"\22\6\u016f\u0170\b"+
		"\22\1\2\u0170\u017c\3\2\2\2\u0171\u0172\f\4\2\2\u0172\u0173\t\5\2\2\u0173"+
		"\u0174\5\"\22\5\u0174\u0175\b\22\1\2\u0175\u017c\3\2\2\2\u0176\u0177\f"+
		"\3\2\2\u0177\u0178\t\6\2\2\u0178\u0179\5\"\22\4\u0179\u017a\b\22\1\2\u017a"+
		"\u017c\3\2\2\2\u017b\u0167\3\2\2\2\u017b\u016c\3\2\2\2\u017b\u0171\3\2"+
		"\2\2\u017b\u0176\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b\3\2\2\2\u017d"+
		"\u017e\3\2\2\2\u017e#\3\2\2\2\u017f\u017d\3\2\2\2\u0180\u0181\7\35\2\2"+
		"\u0181\u0189\b\23\1\2\u0182\u0183\7 \2\2\u0183\u0189\b\23\1\2\u0184\u0185"+
		"\7\36\2\2\u0185\u0189\b\23\1\2\u0186\u0187\7\37\2\2\u0187\u0189\b\23\1"+
		"\2\u0188\u0180\3\2\2\2\u0188\u0182\3\2\2\2\u0188\u0184\3\2\2\2\u0188\u0186"+
		"\3\2\2\2\u0189%\3\2\2\2\63.\67:EIMWagjnr{\u0080\u0086\u0094\u009f\u00a9"+
		"\u00ba\u00cf\u00d2\u00d6\u00d9\u00dc\u00e9\u00ed\u00f2\u00f5\u00f9\u00fd"+
		"\u0101\u0106\u0109\u0111\u0115\u011a\u011d\u0122\u0127\u012b\u0130\u0133"+
		"\u013f\u014b\u014e\u0165\u017b\u017d\u0188";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}