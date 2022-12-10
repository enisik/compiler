// Generated from /home/ensar/Documents/Compilerbau/compiler/GoParser.g4 by ANTLR 4.9.2
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
		VAR=1, RETURN=2, FUNC=3, PACKAGE=4, IMPORT=5, MAIN=6, IF=7, ELSE=8, FOR=9, 
		INT_TYPE=10, FLOAT_TYPE=11, BOOL_TYPE=12, STRING_TYPE=13, PLUS=14, MINUS=15, 
		STAR=16, DIVISON=17, MODULO=18, EQUALS=19, UNEQUAL=20, LESS=21, GREATER=22, 
		LESSEQUAL=23, GREATEREQUAL=24, AND=25, OR=26, NOT=27, INTEGER=28, FLOAT=29, 
		BOOL=30, STRING=31, NL=32, LB=33, RB=34, CLB=35, CRB=36, COMMA=37, DOT=38, 
		SEMICOLON=39, IS=40, WHITESPACE=41, COMMENT=42, IDENTIFIER=43;
	public static final int
		RULE_program = 0, RULE_main_method = 1, RULE_methods = 2, RULE_method = 3, 
		RULE_body = 4, RULE_func_args = 5, RULE_type = 6, RULE_declarations = 7, 
		RULE_declaration = 8, RULE_statements = 9, RULE_statement = 10, RULE_block_stmt = 11, 
		RULE_assignment = 12, RULE_if_control = 13, RULE_for_control = 14, RULE_func_call = 15, 
		RULE_expr = 16, RULE_literals = 17;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "main_method", "methods", "method", "body", "func_args", "type", 
			"declarations", "declaration", "statements", "statement", "block_stmt", 
			"assignment", "if_control", "for_control", "func_call", "expr", "literals"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'var'", "'return'", "'func'", "'package'", "'import'", "'main'", 
			"'if'", "'else'", "'for'", "'int'", "'float64'", "'bool'", "'string'", 
			"'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'>'", "'<='", 
			"'>='", "'&&'", "'||'", "'!'", null, null, null, null, null, "'('", "')'", 
			"'{'", "'}'", "','", "'.'", "';'", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "VAR", "RETURN", "FUNC", "PACKAGE", "IMPORT", "MAIN", "IF", "ELSE", 
			"FOR", "INT_TYPE", "FLOAT_TYPE", "BOOL_TYPE", "STRING_TYPE", "PLUS", 
			"MINUS", "STAR", "DIVISON", "MODULO", "EQUALS", "UNEQUAL", "LESS", "GREATER", 
			"LESSEQUAL", "GREATEREQUAL", "AND", "OR", "NOT", "INTEGER", "FLOAT", 
			"BOOL", "STRING", "NL", "LB", "RB", "CLB", "CRB", "COMMA", "DOT", "SEMICOLON", 
			"IS", "WHITESPACE", "COMMENT", "IDENTIFIER"
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
		public TerminalNode PACKAGE() { return getToken(GoParser.PACKAGE, 0); }
		public TerminalNode MAIN() { return getToken(GoParser.MAIN, 0); }
		public List<TerminalNode> NL() { return getTokens(GoParser.NL); }
		public TerminalNode NL(int i) {
			return getToken(GoParser.NL, i);
		}
		public Main_methodContext main_method() {
			return getRuleContext(Main_methodContext.class,0);
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
		public MethodsContext methods() {
			return getRuleContext(MethodsContext.class,0);
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
			match(MAIN);
			setState(38);
			match(NL);
			setState(43);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==IMPORT) {
				{
				{
				setState(39);
				match(IMPORT);
				setState(40);
				match(STRING);
				}
				}
				setState(45);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(46);
			match(NL);
			setState(47);
			main_method();
			setState(50);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(48);
				match(NL);
				setState(49);
				methods();
				}
				break;
			}
			setState(53);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(52);
				match(NL);
				}
			}

			setState(55);
			match(EOF);
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

	public static class Main_methodContext extends ParserRuleContext {
		public TerminalNode FUNC() { return getToken(GoParser.FUNC, 0); }
		public TerminalNode MAIN() { return getToken(GoParser.MAIN, 0); }
		public TerminalNode LB() { return getToken(GoParser.LB, 0); }
		public TerminalNode RB() { return getToken(GoParser.RB, 0); }
		public TerminalNode CLB() { return getToken(GoParser.CLB, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public TerminalNode CRB() { return getToken(GoParser.CRB, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public List<TerminalNode> NL() { return getTokens(GoParser.NL); }
		public TerminalNode NL(int i) {
			return getToken(GoParser.NL, i);
		}
		public Main_methodContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main_method; }
	}

	public final Main_methodContext main_method() throws RecognitionException {
		Main_methodContext _localctx = new Main_methodContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_main_method);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(57);
			match(FUNC);
			setState(58);
			match(MAIN);
			setState(59);
			match(LB);
			setState(60);
			match(RB);
			setState(62);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT_TYPE) | (1L << FLOAT_TYPE) | (1L << BOOL_TYPE) | (1L << STRING_TYPE))) != 0)) {
				{
				setState(61);
				type();
				}
			}

			setState(65);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(64);
				match(NL);
				}
			}

			setState(67);
			match(CLB);
			setState(69);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				setState(68);
				match(NL);
				}
				break;
			}
			setState(71);
			body();
			setState(73);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(72);
				match(NL);
				}
			}

			setState(75);
			match(CRB);
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

	public static class MethodsContext extends ParserRuleContext {
		public MethodContext method() {
			return getRuleContext(MethodContext.class,0);
		}
		public TerminalNode NL() { return getToken(GoParser.NL, 0); }
		public MethodsContext methods() {
			return getRuleContext(MethodsContext.class,0);
		}
		public MethodsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methods; }
	}

	public final MethodsContext methods() throws RecognitionException {
		MethodsContext _localctx = new MethodsContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_methods);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			method();
			setState(80);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				{
				setState(78);
				match(NL);
				setState(79);
				methods();
				}
				break;
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

	public static class MethodContext extends ParserRuleContext {
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
		public MethodContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method; }
	}

	public final MethodContext method() throws RecognitionException {
		MethodContext _localctx = new MethodContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_method);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			match(FUNC);
			setState(83);
			match(IDENTIFIER);
			setState(84);
			match(LB);
			setState(86);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IDENTIFIER) {
				{
				setState(85);
				func_args();
				}
			}

			setState(88);
			match(RB);
			setState(90);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT_TYPE) | (1L << FLOAT_TYPE) | (1L << BOOL_TYPE) | (1L << STRING_TYPE))) != 0)) {
				{
				setState(89);
				type();
				}
			}

			setState(93);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(92);
				match(NL);
				}
			}

			setState(95);
			match(CLB);
			setState(97);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(96);
				match(NL);
				}
				break;
			}
			setState(99);
			body();
			setState(101);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(100);
				match(NL);
				}
			}

			setState(103);
			match(CRB);
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
		public DeclarationsContext declarations() {
			return getRuleContext(DeclarationsContext.class,0);
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
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==VAR) {
				{
				setState(105);
				declarations();
				}
			}

			setState(109);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << RETURN) | (1L << IF) | (1L << FOR) | (1L << CLB) | (1L << IDENTIFIER))) != 0)) {
				{
				setState(108);
				statements();
				}
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

	public static class Func_argsContext extends ParserRuleContext {
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
			setState(111);
			match(IDENTIFIER);
			setState(112);
			type();
			setState(118);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(113);
				match(COMMA);
				setState(114);
				match(IDENTIFIER);
				setState(115);
				type();
				}
				}
				setState(120);
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
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(121);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT_TYPE) | (1L << FLOAT_TYPE) | (1L << BOOL_TYPE) | (1L << STRING_TYPE))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
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

	public static class DeclarationsContext extends ParserRuleContext {
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
			setState(130);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(123);
				declaration();
				setState(124);
				match(NL);
				setState(125);
				declarations();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(127);
				declaration();
				setState(128);
				match(NL);
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
		public TerminalNode VAR() { return getToken(GoParser.VAR, 0); }
		public TerminalNode IDENTIFIER() { return getToken(GoParser.IDENTIFIER, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode IS() { return getToken(GoParser.IS, 0); }
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
			setState(132);
			match(VAR);
			setState(133);
			match(IDENTIFIER);
			setState(134);
			type();
			setState(135);
			match(IS);
			setState(136);
			expr(0);
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
			setState(145);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(138);
				statement();
				setState(139);
				match(NL);
				setState(140);
				statements();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(142);
				statement();
				setState(143);
				match(NL);
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
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public Block_stmtContext block_stmt() {
			return getRuleContext(Block_stmtContext.class,0);
		}
		public If_controlContext if_control() {
			return getRuleContext(If_controlContext.class,0);
		}
		public For_controlContext for_control() {
			return getRuleContext(For_controlContext.class,0);
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
		try {
			setState(154);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(147);
				assignment();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(148);
				block_stmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(149);
				if_control();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(150);
				for_control();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(151);
				func_call();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(152);
				match(RETURN);
				setState(153);
				expr(0);
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
		public TerminalNode CLB() { return getToken(GoParser.CLB, 0); }
		public StatementsContext statements() {
			return getRuleContext(StatementsContext.class,0);
		}
		public TerminalNode CRB() { return getToken(GoParser.CRB, 0); }
		public List<TerminalNode> NL() { return getTokens(GoParser.NL); }
		public TerminalNode NL(int i) {
			return getToken(GoParser.NL, i);
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
			setState(156);
			match(CLB);
			setState(158);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(157);
				match(NL);
				}
			}

			setState(160);
			statements();
			setState(162);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(161);
				match(NL);
				}
			}

			setState(164);
			match(CRB);
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
		public TerminalNode IDENTIFIER() { return getToken(GoParser.IDENTIFIER, 0); }
		public TerminalNode IS() { return getToken(GoParser.IS, 0); }
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
			setState(166);
			match(IDENTIFIER);
			setState(167);
			match(IS);
			setState(168);
			expr(0);
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
			setState(219);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,33,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(170);
				match(IF);
				setState(171);
				expr(0);
				setState(173);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NL) {
					{
					setState(172);
					match(NL);
					}
				}

				setState(175);
				match(CLB);
				setState(177);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
				case 1:
					{
					setState(176);
					match(NL);
					}
					break;
				}
				setState(180);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << RETURN) | (1L << IF) | (1L << FOR) | (1L << CLB) | (1L << IDENTIFIER))) != 0)) {
					{
					setState(179);
					statements();
					}
				}

				setState(183);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NL) {
					{
					setState(182);
					match(NL);
					}
				}

				setState(185);
				match(CRB);
				setState(187);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NL) {
					{
					setState(186);
					match(NL);
					}
				}

				setState(189);
				match(ELSE);
				setState(191);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NL) {
					{
					setState(190);
					match(NL);
					}
				}

				setState(193);
				match(CLB);
				setState(195);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
				case 1:
					{
					setState(194);
					match(NL);
					}
					break;
				}
				setState(198);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << RETURN) | (1L << IF) | (1L << FOR) | (1L << CLB) | (1L << IDENTIFIER))) != 0)) {
					{
					setState(197);
					statements();
					}
				}

				setState(201);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NL) {
					{
					setState(200);
					match(NL);
					}
				}

				setState(203);
				match(CRB);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(205);
				match(IF);
				setState(206);
				expr(0);
				setState(208);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NL) {
					{
					setState(207);
					match(NL);
					}
				}

				setState(210);
				match(CLB);
				setState(212);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NL) {
					{
					setState(211);
					match(NL);
					}
				}

				setState(215);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << RETURN) | (1L << IF) | (1L << FOR) | (1L << CLB) | (1L << IDENTIFIER))) != 0)) {
					{
					setState(214);
					statements();
					}
				}

				setState(217);
				match(CRB);
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

	public static class For_controlContext extends ParserRuleContext {
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
		public For_controlContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_control; }
	}

	public final For_controlContext for_control() throws RecognitionException {
		For_controlContext _localctx = new For_controlContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_for_control);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(221);
			match(FOR);
			setState(222);
			expr(0);
			setState(224);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(223);
				match(NL);
				}
			}

			setState(226);
			match(CLB);
			setState(228);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,35,_ctx) ) {
			case 1:
				{
				setState(227);
				match(NL);
				}
				break;
			}
			setState(231);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << RETURN) | (1L << IF) | (1L << FOR) | (1L << CLB) | (1L << IDENTIFIER))) != 0)) {
				{
				setState(230);
				statements();
				}
			}

			setState(234);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(233);
				match(NL);
				}
			}

			setState(236);
			match(CRB);
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
		public List<TerminalNode> IDENTIFIER() { return getTokens(GoParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(GoParser.IDENTIFIER, i);
		}
		public TerminalNode LB() { return getToken(GoParser.LB, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode RB() { return getToken(GoParser.RB, 0); }
		public List<TerminalNode> DOT() { return getTokens(GoParser.DOT); }
		public TerminalNode DOT(int i) {
			return getToken(GoParser.DOT, i);
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
			setState(238);
			match(IDENTIFIER);
			setState(243);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DOT) {
				{
				{
				setState(239);
				match(DOT);
				setState(240);
				match(IDENTIFIER);
				}
				}
				setState(245);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(246);
			match(LB);
			setState(247);
			expr(0);
			setState(252);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(248);
				match(COMMA);
				setState(249);
				expr(0);
				}
				}
				setState(254);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(255);
			match(RB);
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
			setState(267);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,40,_ctx) ) {
			case 1:
				{
				setState(258);
				match(IDENTIFIER);
				}
				break;
			case 2:
				{
				setState(259);
				func_call();
				}
				break;
			case 3:
				{
				setState(260);
				literals();
				}
				break;
			case 4:
				{
				setState(261);
				match(LB);
				setState(262);
				expr(0);
				setState(263);
				match(RB);
				}
				break;
			case 5:
				{
				setState(265);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PLUS) | (1L << MINUS) | (1L << NOT))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(266);
				expr(5);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(283);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,42,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(281);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,41,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(269);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(270);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << STAR) | (1L << DIVISON) | (1L << MODULO))) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(271);
						expr(5);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(272);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(273);
						_la = _input.LA(1);
						if ( !(_la==PLUS || _la==MINUS) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(274);
						expr(4);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(275);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(276);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQUALS) | (1L << UNEQUAL) | (1L << LESS) | (1L << GREATER) | (1L << LESSEQUAL) | (1L << GREATEREQUAL))) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(277);
						expr(3);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(278);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(279);
						_la = _input.LA(1);
						if ( !(_la==AND || _la==OR) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(280);
						expr(2);
						}
						break;
					}
					} 
				}
				setState(285);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,42,_ctx);
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
			setState(294);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTEGER:
				enterOuterAlt(_localctx, 1);
				{
				setState(286);
				((LiteralsContext)_localctx).INTEGER = match(INTEGER);
				print(self.node(int((((LiteralsContext)_localctx).INTEGER!=null?((LiteralsContext)_localctx).INTEGER.getText():null))))
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(288);
				((LiteralsContext)_localctx).STRING = match(STRING);
				print(self.node((((LiteralsContext)_localctx).STRING!=null?((LiteralsContext)_localctx).STRING.getText():null)))
				}
				break;
			case FLOAT:
				enterOuterAlt(_localctx, 3);
				{
				setState(290);
				((LiteralsContext)_localctx).FLOAT = match(FLOAT);
				print(self.node(float((((LiteralsContext)_localctx).FLOAT!=null?((LiteralsContext)_localctx).FLOAT.getText():null))))
				}
				break;
			case BOOL:
				enterOuterAlt(_localctx, 4);
				{
				setState(292);
				((LiteralsContext)_localctx).BOOL = match(BOOL);
				print(self.node((((LiteralsContext)_localctx).BOOL!=null?((LiteralsContext)_localctx).BOOL.getText():null) != 'false'))
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
		case 16:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 4);
		case 1:
			return precpred(_ctx, 3);
		case 2:
			return precpred(_ctx, 2);
		case 3:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3-\u012b\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\3\2\3\2\3\2\3\2\3\2\7\2,\n\2\f\2\16\2/\13\2\3\2\3\2\3\2\3\2"+
		"\5\2\65\n\2\3\2\5\28\n\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3A\n\3\3\3\5\3"+
		"D\n\3\3\3\3\3\5\3H\n\3\3\3\3\3\5\3L\n\3\3\3\3\3\3\4\3\4\3\4\5\4S\n\4\3"+
		"\5\3\5\3\5\3\5\5\5Y\n\5\3\5\3\5\5\5]\n\5\3\5\5\5`\n\5\3\5\3\5\5\5d\n\5"+
		"\3\5\3\5\5\5h\n\5\3\5\3\5\3\6\5\6m\n\6\3\6\5\6p\n\6\3\7\3\7\3\7\3\7\3"+
		"\7\7\7w\n\7\f\7\16\7z\13\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u0085"+
		"\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u0094"+
		"\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u009d\n\f\3\r\3\r\5\r\u00a1\n\r"+
		"\3\r\3\r\5\r\u00a5\n\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\5\17"+
		"\u00b0\n\17\3\17\3\17\5\17\u00b4\n\17\3\17\5\17\u00b7\n\17\3\17\5\17\u00ba"+
		"\n\17\3\17\3\17\5\17\u00be\n\17\3\17\3\17\5\17\u00c2\n\17\3\17\3\17\5"+
		"\17\u00c6\n\17\3\17\5\17\u00c9\n\17\3\17\5\17\u00cc\n\17\3\17\3\17\3\17"+
		"\3\17\3\17\5\17\u00d3\n\17\3\17\3\17\5\17\u00d7\n\17\3\17\5\17\u00da\n"+
		"\17\3\17\3\17\5\17\u00de\n\17\3\20\3\20\3\20\5\20\u00e3\n\20\3\20\3\20"+
		"\5\20\u00e7\n\20\3\20\5\20\u00ea\n\20\3\20\5\20\u00ed\n\20\3\20\3\20\3"+
		"\21\3\21\3\21\7\21\u00f4\n\21\f\21\16\21\u00f7\13\21\3\21\3\21\3\21\3"+
		"\21\7\21\u00fd\n\21\f\21\16\21\u0100\13\21\3\21\3\21\3\22\3\22\3\22\3"+
		"\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u010e\n\22\3\22\3\22\3\22\3\22"+
		"\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u011c\n\22\f\22\16\22\u011f"+
		"\13\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0129\n\23\3\23\2"+
		"\3\"\24\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$\2\b\3\2\f\17\4\2\20"+
		"\21\35\35\3\2\22\24\3\2\20\21\3\2\25\32\3\2\33\34\2\u014f\2&\3\2\2\2\4"+
		";\3\2\2\2\6O\3\2\2\2\bT\3\2\2\2\nl\3\2\2\2\fq\3\2\2\2\16{\3\2\2\2\20\u0084"+
		"\3\2\2\2\22\u0086\3\2\2\2\24\u0093\3\2\2\2\26\u009c\3\2\2\2\30\u009e\3"+
		"\2\2\2\32\u00a8\3\2\2\2\34\u00dd\3\2\2\2\36\u00df\3\2\2\2 \u00f0\3\2\2"+
		"\2\"\u010d\3\2\2\2$\u0128\3\2\2\2&\'\7\6\2\2\'(\7\b\2\2(-\7\"\2\2)*\7"+
		"\7\2\2*,\7!\2\2+)\3\2\2\2,/\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\60\3\2\2\2/-"+
		"\3\2\2\2\60\61\7\"\2\2\61\64\5\4\3\2\62\63\7\"\2\2\63\65\5\6\4\2\64\62"+
		"\3\2\2\2\64\65\3\2\2\2\65\67\3\2\2\2\668\7\"\2\2\67\66\3\2\2\2\678\3\2"+
		"\2\289\3\2\2\29:\7\2\2\3:\3\3\2\2\2;<\7\5\2\2<=\7\b\2\2=>\7#\2\2>@\7$"+
		"\2\2?A\5\16\b\2@?\3\2\2\2@A\3\2\2\2AC\3\2\2\2BD\7\"\2\2CB\3\2\2\2CD\3"+
		"\2\2\2DE\3\2\2\2EG\7%\2\2FH\7\"\2\2GF\3\2\2\2GH\3\2\2\2HI\3\2\2\2IK\5"+
		"\n\6\2JL\7\"\2\2KJ\3\2\2\2KL\3\2\2\2LM\3\2\2\2MN\7&\2\2N\5\3\2\2\2OR\5"+
		"\b\5\2PQ\7\"\2\2QS\5\6\4\2RP\3\2\2\2RS\3\2\2\2S\7\3\2\2\2TU\7\5\2\2UV"+
		"\7-\2\2VX\7#\2\2WY\5\f\7\2XW\3\2\2\2XY\3\2\2\2YZ\3\2\2\2Z\\\7$\2\2[]\5"+
		"\16\b\2\\[\3\2\2\2\\]\3\2\2\2]_\3\2\2\2^`\7\"\2\2_^\3\2\2\2_`\3\2\2\2"+
		"`a\3\2\2\2ac\7%\2\2bd\7\"\2\2cb\3\2\2\2cd\3\2\2\2de\3\2\2\2eg\5\n\6\2"+
		"fh\7\"\2\2gf\3\2\2\2gh\3\2\2\2hi\3\2\2\2ij\7&\2\2j\t\3\2\2\2km\5\20\t"+
		"\2lk\3\2\2\2lm\3\2\2\2mo\3\2\2\2np\5\24\13\2on\3\2\2\2op\3\2\2\2p\13\3"+
		"\2\2\2qr\7-\2\2rx\5\16\b\2st\7\'\2\2tu\7-\2\2uw\5\16\b\2vs\3\2\2\2wz\3"+
		"\2\2\2xv\3\2\2\2xy\3\2\2\2y\r\3\2\2\2zx\3\2\2\2{|\t\2\2\2|\17\3\2\2\2"+
		"}~\5\22\n\2~\177\7\"\2\2\177\u0080\5\20\t\2\u0080\u0085\3\2\2\2\u0081"+
		"\u0082\5\22\n\2\u0082\u0083\7\"\2\2\u0083\u0085\3\2\2\2\u0084}\3\2\2\2"+
		"\u0084\u0081\3\2\2\2\u0085\21\3\2\2\2\u0086\u0087\7\3\2\2\u0087\u0088"+
		"\7-\2\2\u0088\u0089\5\16\b\2\u0089\u008a\7*\2\2\u008a\u008b\5\"\22\2\u008b"+
		"\23\3\2\2\2\u008c\u008d\5\26\f\2\u008d\u008e\7\"\2\2\u008e\u008f\5\24"+
		"\13\2\u008f\u0094\3\2\2\2\u0090\u0091\5\26\f\2\u0091\u0092\7\"\2\2\u0092"+
		"\u0094\3\2\2\2\u0093\u008c\3\2\2\2\u0093\u0090\3\2\2\2\u0094\25\3\2\2"+
		"\2\u0095\u009d\5\32\16\2\u0096\u009d\5\30\r\2\u0097\u009d\5\34\17\2\u0098"+
		"\u009d\5\36\20\2\u0099\u009d\5 \21\2\u009a\u009b\7\4\2\2\u009b\u009d\5"+
		"\"\22\2\u009c\u0095\3\2\2\2\u009c\u0096\3\2\2\2\u009c\u0097\3\2\2\2\u009c"+
		"\u0098\3\2\2\2\u009c\u0099\3\2\2\2\u009c\u009a\3\2\2\2\u009d\27\3\2\2"+
		"\2\u009e\u00a0\7%\2\2\u009f\u00a1\7\"\2\2\u00a0\u009f\3\2\2\2\u00a0\u00a1"+
		"\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a4\5\24\13\2\u00a3\u00a5\7\"\2\2"+
		"\u00a4\u00a3\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7"+
		"\7&\2\2\u00a7\31\3\2\2\2\u00a8\u00a9\7-\2\2\u00a9\u00aa\7*\2\2\u00aa\u00ab"+
		"\5\"\22\2\u00ab\33\3\2\2\2\u00ac\u00ad\7\t\2\2\u00ad\u00af\5\"\22\2\u00ae"+
		"\u00b0\7\"\2\2\u00af\u00ae\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b1\3\2"+
		"\2\2\u00b1\u00b3\7%\2\2\u00b2\u00b4\7\"\2\2\u00b3\u00b2\3\2\2\2\u00b3"+
		"\u00b4\3\2\2\2\u00b4\u00b6\3\2\2\2\u00b5\u00b7\5\24\13\2\u00b6\u00b5\3"+
		"\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b9\3\2\2\2\u00b8\u00ba\7\"\2\2\u00b9"+
		"\u00b8\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bd\7&"+
		"\2\2\u00bc\u00be\7\"\2\2\u00bd\u00bc\3\2\2\2\u00bd\u00be\3\2\2\2\u00be"+
		"\u00bf\3\2\2\2\u00bf\u00c1\7\n\2\2\u00c0\u00c2\7\"\2\2\u00c1\u00c0\3\2"+
		"\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c5\7%\2\2\u00c4"+
		"\u00c6\7\"\2\2\u00c5\u00c4\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c8\3\2"+
		"\2\2\u00c7\u00c9\5\24\13\2\u00c8\u00c7\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9"+
		"\u00cb\3\2\2\2\u00ca\u00cc\7\"\2\2\u00cb\u00ca\3\2\2\2\u00cb\u00cc\3\2"+
		"\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce\7&\2\2\u00ce\u00de\3\2\2\2\u00cf"+
		"\u00d0\7\t\2\2\u00d0\u00d2\5\"\22\2\u00d1\u00d3\7\"\2\2\u00d2\u00d1\3"+
		"\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d6\7%\2\2\u00d5"+
		"\u00d7\7\"\2\2\u00d6\u00d5\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d9\3\2"+
		"\2\2\u00d8\u00da\5\24\13\2\u00d9\u00d8\3\2\2\2\u00d9\u00da\3\2\2\2\u00da"+
		"\u00db\3\2\2\2\u00db\u00dc\7&\2\2\u00dc\u00de\3\2\2\2\u00dd\u00ac\3\2"+
		"\2\2\u00dd\u00cf\3\2\2\2\u00de\35\3\2\2\2\u00df\u00e0\7\13\2\2\u00e0\u00e2"+
		"\5\"\22\2\u00e1\u00e3\7\"\2\2\u00e2\u00e1\3\2\2\2\u00e2\u00e3\3\2\2\2"+
		"\u00e3\u00e4\3\2\2\2\u00e4\u00e6\7%\2\2\u00e5\u00e7\7\"\2\2\u00e6\u00e5"+
		"\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e9\3\2\2\2\u00e8\u00ea\5\24\13\2"+
		"\u00e9\u00e8\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00ec\3\2\2\2\u00eb\u00ed"+
		"\7\"\2\2\u00ec\u00eb\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee"+
		"\u00ef\7&\2\2\u00ef\37\3\2\2\2\u00f0\u00f5\7-\2\2\u00f1\u00f2\7(\2\2\u00f2"+
		"\u00f4\7-\2\2\u00f3\u00f1\3\2\2\2\u00f4\u00f7\3\2\2\2\u00f5\u00f3\3\2"+
		"\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f8\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8"+
		"\u00f9\7#\2\2\u00f9\u00fe\5\"\22\2\u00fa\u00fb\7\'\2\2\u00fb\u00fd\5\""+
		"\22\2\u00fc\u00fa\3\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe"+
		"\u00ff\3\2\2\2\u00ff\u0101\3\2\2\2\u0100\u00fe\3\2\2\2\u0101\u0102\7$"+
		"\2\2\u0102!\3\2\2\2\u0103\u0104\b\22\1\2\u0104\u010e\7-\2\2\u0105\u010e"+
		"\5 \21\2\u0106\u010e\5$\23\2\u0107\u0108\7#\2\2\u0108\u0109\5\"\22\2\u0109"+
		"\u010a\7$\2\2\u010a\u010e\3\2\2\2\u010b\u010c\t\3\2\2\u010c\u010e\5\""+
		"\22\7\u010d\u0103\3\2\2\2\u010d\u0105\3\2\2\2\u010d\u0106\3\2\2\2\u010d"+
		"\u0107\3\2\2\2\u010d\u010b\3\2\2\2\u010e\u011d\3\2\2\2\u010f\u0110\f\6"+
		"\2\2\u0110\u0111\t\4\2\2\u0111\u011c\5\"\22\7\u0112\u0113\f\5\2\2\u0113"+
		"\u0114\t\5\2\2\u0114\u011c\5\"\22\6\u0115\u0116\f\4\2\2\u0116\u0117\t"+
		"\6\2\2\u0117\u011c\5\"\22\5\u0118\u0119\f\3\2\2\u0119\u011a\t\7\2\2\u011a"+
		"\u011c\5\"\22\4\u011b\u010f\3\2\2\2\u011b\u0112\3\2\2\2\u011b\u0115\3"+
		"\2\2\2\u011b\u0118\3\2\2\2\u011c\u011f\3\2\2\2\u011d\u011b\3\2\2\2\u011d"+
		"\u011e\3\2\2\2\u011e#\3\2\2\2\u011f\u011d\3\2\2\2\u0120\u0121\7\36\2\2"+
		"\u0121\u0129\b\23\1\2\u0122\u0123\7!\2\2\u0123\u0129\b\23\1\2\u0124\u0125"+
		"\7\37\2\2\u0125\u0129\b\23\1\2\u0126\u0127\7 \2\2\u0127\u0129\b\23\1\2"+
		"\u0128\u0120\3\2\2\2\u0128\u0122\3\2\2\2\u0128\u0124\3\2\2\2\u0128\u0126"+
		"\3\2\2\2\u0129%\3\2\2\2.-\64\67@CGKRX\\_cglox\u0084\u0093\u009c\u00a0"+
		"\u00a4\u00af\u00b3\u00b6\u00b9\u00bd\u00c1\u00c5\u00c8\u00cb\u00d2\u00d6"+
		"\u00d9\u00dd\u00e2\u00e6\u00e9\u00ec\u00f5\u00fe\u010d\u011b\u011d\u0128";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}