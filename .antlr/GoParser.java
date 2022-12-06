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
public class GoParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PLUS=1, MINUS=2, STAR=3, DIVISON=4, MODULO=5, EQUALS=6, UNEQUAL=7, LESS=8, 
		GREATER=9, LESSEQUAL=10, GREATEREQUAL=11, AND=12, OR=13, NOT=14, INT_TYPE=15, 
		FLOAT_TYPE=16, BOOL_TYPE=17, STRING_TYPE=18, IF=19, ELSE=20, FOR=21, INTEGER=22, 
		FLOAT=23, BOOL=24, STRING=25, VAR=26, RETURN=27, FUNC=28, PACKAGE=29, 
		IMPORT=30, MAIN=31, PRINT=32, NL=33, LB=34, RB=35, CLB=36, CRB=37, COMMA=38, 
		SEMICOLON=39, IS=40, WHITESPACE=41, IDENTIFIER=42, COMMENT=43;
	public static final int
		RULE_program = 0, RULE_main_method = 1, RULE_methods = 2, RULE_body = 3, 
		RULE_func_args = 4, RULE_type = 5, RULE_declarations = 6, RULE_declaration = 7, 
		RULE_statements = 8, RULE_statement = 9, RULE_expr = 10, RULE_opt_return = 11, 
		RULE_literals = 12, RULE_if_control = 13, RULE_for_control = 14;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "main_method", "methods", "body", "func_args", "type", "declarations", 
			"declaration", "statements", "statement", "expr", "opt_return", "literals", 
			"if_control", "for_control"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'>'", 
			"'<='", "'>='", "'&&'", "'||'", "'!'", "'int'", "'float'", "'bool'", 
			"'string'", "'if'", "'else'", "'for'", null, null, null, null, "'var'", 
			"'return'", "'func'", "'package main'", "'import \"fmt\"'", "'main'", 
			"'fmt.Println'", null, "'('", "')'", "'{'", "'}'", "','", "';'", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PLUS", "MINUS", "STAR", "DIVISON", "MODULO", "EQUALS", "UNEQUAL", 
			"LESS", "GREATER", "LESSEQUAL", "GREATEREQUAL", "AND", "OR", "NOT", "INT_TYPE", 
			"FLOAT_TYPE", "BOOL_TYPE", "STRING_TYPE", "IF", "ELSE", "FOR", "INTEGER", 
			"FLOAT", "BOOL", "STRING", "VAR", "RETURN", "FUNC", "PACKAGE", "IMPORT", 
			"MAIN", "PRINT", "NL", "LB", "RB", "CLB", "CRB", "COMMA", "SEMICOLON", 
			"IS", "WHITESPACE", "IDENTIFIER", "COMMENT"
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
		public List<TerminalNode> NL() { return getTokens(GoParser.NL); }
		public TerminalNode NL(int i) {
			return getToken(GoParser.NL, i);
		}
		public TerminalNode IMPORT() { return getToken(GoParser.IMPORT, 0); }
		public Main_methodContext main_method() {
			return getRuleContext(Main_methodContext.class,0);
		}
		public TerminalNode EOF() { return getToken(GoParser.EOF, 0); }
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
			setState(30);
			match(PACKAGE);
			setState(31);
			match(NL);
			setState(32);
			match(IMPORT);
			setState(33);
			match(NL);
			setState(34);
			main_method();
			setState(37);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				{
				setState(35);
				match(NL);
				setState(36);
				methods();
				}
				break;
			}
			setState(40);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(39);
				match(NL);
				}
			}

			setState(42);
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
			setState(44);
			match(FUNC);
			setState(45);
			match(MAIN);
			setState(46);
			match(LB);
			setState(47);
			match(RB);
			setState(49);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT_TYPE) | (1L << FLOAT_TYPE) | (1L << BOOL_TYPE) | (1L << STRING_TYPE))) != 0)) {
				{
				setState(48);
				type();
				}
			}

			setState(52);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(51);
				match(NL);
				}
			}

			setState(54);
			match(CLB);
			setState(56);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(55);
				match(NL);
				}
				break;
			}
			setState(58);
			body();
			setState(60);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(59);
				match(NL);
				}
			}

			setState(62);
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
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			match(FUNC);
			setState(65);
			match(IDENTIFIER);
			setState(66);
			match(LB);
			setState(68);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IDENTIFIER) {
				{
				setState(67);
				func_args();
				}
			}

			setState(70);
			match(RB);
			setState(72);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT_TYPE) | (1L << FLOAT_TYPE) | (1L << BOOL_TYPE) | (1L << STRING_TYPE))) != 0)) {
				{
				setState(71);
				type();
				}
			}

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
			match(CLB);
			setState(79);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				setState(78);
				match(NL);
				}
				break;
			}
			setState(81);
			body();
			setState(83);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(82);
				match(NL);
				}
			}

			setState(85);
			match(CRB);
			setState(88);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(86);
				match(NL);
				setState(87);
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

	public static class BodyContext extends ParserRuleContext {
		public DeclarationsContext declarations() {
			return getRuleContext(DeclarationsContext.class,0);
		}
		public StatementsContext statements() {
			return getRuleContext(StatementsContext.class,0);
		}
		public Opt_returnContext opt_return() {
			return getRuleContext(Opt_returnContext.class,0);
		}
		public BodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body; }
	}

	public final BodyContext body() throws RecognitionException {
		BodyContext _localctx = new BodyContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_body);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				{
				setState(90);
				declarations();
				}
				break;
			}
			setState(94);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IF) | (1L << VAR) | (1L << PRINT) | (1L << CLB))) != 0)) {
				{
				setState(93);
				statements();
				}
			}

			setState(97);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==RETURN) {
				{
				setState(96);
				opt_return();
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
		public TerminalNode IDENTIFIER() { return getToken(GoParser.IDENTIFIER, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(GoParser.COMMA, 0); }
		public Func_argsContext func_args() {
			return getRuleContext(Func_argsContext.class,0);
		}
		public Func_argsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_args; }
	}

	public final Func_argsContext func_args() throws RecognitionException {
		Func_argsContext _localctx = new Func_argsContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_func_args);
		try {
			setState(106);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(99);
				match(IDENTIFIER);
				setState(100);
				type();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(101);
				match(IDENTIFIER);
				setState(102);
				type();
				setState(103);
				match(COMMA);
				setState(104);
				func_args();
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
		enterRule(_localctx, 10, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
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
		public List<DeclarationContext> declaration() {
			return getRuleContexts(DeclarationContext.class);
		}
		public DeclarationContext declaration(int i) {
			return getRuleContext(DeclarationContext.class,i);
		}
		public TerminalNode NL() { return getToken(GoParser.NL, 0); }
		public DeclarationsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declarations; }
	}

	public final DeclarationsContext declarations() throws RecognitionException {
		DeclarationsContext _localctx = new DeclarationsContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_declarations);
		try {
			setState(117);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(110);
				declaration();
				setState(111);
				match(NL);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(113);
				declaration();
				setState(114);
				match(NL);
				setState(115);
				declaration();
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
		enterRule(_localctx, 14, RULE_declaration);
		try {
			setState(128);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(119);
				match(VAR);
				setState(120);
				match(IDENTIFIER);
				setState(121);
				type();
				setState(122);
				match(IS);
				setState(123);
				expr(0);
				}
				break;
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(125);
				match(IDENTIFIER);
				setState(126);
				match(IS);
				setState(127);
				expr(0);
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

	public static class StatementsContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public TerminalNode NL() { return getToken(GoParser.NL, 0); }
		public StatementsContext statements() {
			return getRuleContext(StatementsContext.class,0);
		}
		public TerminalNode CLB() { return getToken(GoParser.CLB, 0); }
		public TerminalNode CRB() { return getToken(GoParser.CRB, 0); }
		public StatementsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statements; }
	}

	public final StatementsContext statements() throws RecognitionException {
		StatementsContext _localctx = new StatementsContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_statements);
		try {
			setState(142);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(130);
				statement();
				setState(131);
				match(NL);
				setState(132);
				statements();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(134);
				match(CLB);
				setState(135);
				statements();
				setState(136);
				match(CRB);
				setState(137);
				match(NL);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(139);
				statement();
				setState(140);
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
		public TerminalNode VAR() { return getToken(GoParser.VAR, 0); }
		public TerminalNode IS() { return getToken(GoParser.IS, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode IF() { return getToken(GoParser.IF, 0); }
		public TerminalNode CLB() { return getToken(GoParser.CLB, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public TerminalNode CRB() { return getToken(GoParser.CRB, 0); }
		public TerminalNode NL() { return getToken(GoParser.NL, 0); }
		public TerminalNode PRINT() { return getToken(GoParser.PRINT, 0); }
		public TerminalNode LB() { return getToken(GoParser.LB, 0); }
		public TerminalNode RB() { return getToken(GoParser.RB, 0); }
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_statement);
		int _la;
		try {
			setState(161);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(144);
				match(VAR);
				setState(145);
				match(IS);
				setState(146);
				expr(0);
				}
				break;
			case IF:
				enterOuterAlt(_localctx, 2);
				{
				setState(147);
				match(IF);
				setState(148);
				expr(0);
				setState(149);
				match(CLB);
				setState(151);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NL) {
					{
					setState(150);
					match(NL);
					}
				}

				setState(153);
				body();
				setState(154);
				match(CRB);
				}
				break;
			case PRINT:
				enterOuterAlt(_localctx, 3);
				{
				setState(156);
				match(PRINT);
				setState(157);
				match(LB);
				setState(158);
				expr(0);
				setState(159);
				match(RB);
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

	public static class ExprContext extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(GoParser.NOT, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode PLUS() { return getToken(GoParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(GoParser.MINUS, 0); }
		public TerminalNode LB() { return getToken(GoParser.LB, 0); }
		public TerminalNode RB() { return getToken(GoParser.RB, 0); }
		public TerminalNode IDENTIFIER() { return getToken(GoParser.IDENTIFIER, 0); }
		public LiteralsContext literals() {
			return getRuleContext(LiteralsContext.class,0);
		}
		public TerminalNode OR() { return getToken(GoParser.OR, 0); }
		public TerminalNode AND() { return getToken(GoParser.AND, 0); }
		public TerminalNode UNEQUAL() { return getToken(GoParser.UNEQUAL, 0); }
		public TerminalNode EQUALS() { return getToken(GoParser.EQUALS, 0); }
		public TerminalNode LESS() { return getToken(GoParser.LESS, 0); }
		public TerminalNode GREATER() { return getToken(GoParser.GREATER, 0); }
		public TerminalNode LESSEQUAL() { return getToken(GoParser.LESSEQUAL, 0); }
		public TerminalNode GREATEREQUAL() { return getToken(GoParser.GREATEREQUAL, 0); }
		public TerminalNode STAR() { return getToken(GoParser.STAR, 0); }
		public TerminalNode DIVISON() { return getToken(GoParser.DIVISON, 0); }
		public TerminalNode MODULO() { return getToken(GoParser.MODULO, 0); }
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
		int _startState = 20;
		enterRecursionRule(_localctx, 20, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(181);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				{
				setState(164);
				match(NOT);
				setState(165);
				expr(7);
				}
				break;
			case 2:
				{
				setState(166);
				match(PLUS);
				setState(167);
				expr(6);
				}
				break;
			case 3:
				{
				setState(168);
				match(MINUS);
				setState(169);
				expr(5);
				}
				break;
			case 4:
				{
				setState(170);
				match(LB);
				setState(171);
				expr(0);
				setState(172);
				match(RB);
				}
				break;
			case 5:
				{
				setState(174);
				match(IDENTIFIER);
				setState(175);
				match(LB);
				setState(176);
				expr(0);
				setState(177);
				match(RB);
				}
				break;
			case 6:
				{
				setState(179);
				literals();
				}
				break;
			case 7:
				{
				setState(180);
				match(IDENTIFIER);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(224);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(222);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(183);
						if (!(precpred(_ctx, 20))) throw new FailedPredicateException(this, "precpred(_ctx, 20)");
						setState(184);
						match(OR);
						setState(185);
						expr(21);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(186);
						if (!(precpred(_ctx, 19))) throw new FailedPredicateException(this, "precpred(_ctx, 19)");
						setState(187);
						match(AND);
						setState(188);
						expr(20);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(189);
						if (!(precpred(_ctx, 18))) throw new FailedPredicateException(this, "precpred(_ctx, 18)");
						setState(190);
						match(UNEQUAL);
						setState(191);
						expr(19);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(192);
						if (!(precpred(_ctx, 17))) throw new FailedPredicateException(this, "precpred(_ctx, 17)");
						setState(193);
						match(EQUALS);
						setState(194);
						expr(18);
						}
						break;
					case 5:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(195);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(196);
						match(LESS);
						setState(197);
						expr(17);
						}
						break;
					case 6:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(198);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(199);
						match(GREATER);
						setState(200);
						expr(16);
						}
						break;
					case 7:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(201);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(202);
						match(LESSEQUAL);
						setState(203);
						expr(15);
						}
						break;
					case 8:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(204);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(205);
						match(GREATEREQUAL);
						setState(206);
						expr(14);
						}
						break;
					case 9:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(207);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(208);
						match(MINUS);
						setState(209);
						expr(13);
						}
						break;
					case 10:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(210);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(211);
						match(PLUS);
						setState(212);
						expr(12);
						}
						break;
					case 11:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(213);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(214);
						match(STAR);
						setState(215);
						expr(11);
						}
						break;
					case 12:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(216);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(217);
						match(DIVISON);
						setState(218);
						expr(10);
						}
						break;
					case 13:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(219);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(220);
						match(MODULO);
						setState(221);
						expr(9);
						}
						break;
					}
					} 
				}
				setState(226);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
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

	public static class Opt_returnContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(GoParser.RETURN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Opt_returnContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opt_return; }
	}

	public final Opt_returnContext opt_return() throws RecognitionException {
		Opt_returnContext _localctx = new Opt_returnContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_opt_return);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(227);
			match(RETURN);
			setState(228);
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

	public static class LiteralsContext extends ParserRuleContext {
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
		enterRule(_localctx, 24, RULE_literals);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(230);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INTEGER) | (1L << FLOAT) | (1L << BOOL) | (1L << STRING))) != 0)) ) {
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

	public static class If_controlContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(GoParser.IF, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public List<TerminalNode> CLB() { return getTokens(GoParser.CLB); }
		public TerminalNode CLB(int i) {
			return getToken(GoParser.CLB, i);
		}
		public List<BodyContext> body() {
			return getRuleContexts(BodyContext.class);
		}
		public BodyContext body(int i) {
			return getRuleContext(BodyContext.class,i);
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
			setState(263);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(232);
				match(IF);
				setState(233);
				expr(0);
				setState(234);
				match(CLB);
				setState(236);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NL) {
					{
					setState(235);
					match(NL);
					}
				}

				setState(238);
				body();
				setState(239);
				match(CRB);
				setState(241);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NL) {
					{
					setState(240);
					match(NL);
					}
				}

				setState(243);
				match(ELSE);
				setState(245);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NL) {
					{
					setState(244);
					match(NL);
					}
				}

				setState(247);
				match(CLB);
				setState(249);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NL) {
					{
					setState(248);
					match(NL);
					}
				}

				setState(251);
				body();
				setState(252);
				match(CRB);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(254);
				match(IF);
				setState(255);
				expr(0);
				setState(256);
				match(CLB);
				setState(258);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==NL) {
					{
					setState(257);
					match(NL);
					}
				}

				setState(260);
				body();
				setState(261);
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
		public StatementsContext statements() {
			return getRuleContext(StatementsContext.class,0);
		}
		public TerminalNode CRB() { return getToken(GoParser.CRB, 0); }
		public For_controlContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_control; }
	}

	public final For_controlContext for_control() throws RecognitionException {
		For_controlContext _localctx = new For_controlContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_for_control);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(265);
			match(FOR);
			setState(266);
			expr(0);
			setState(267);
			match(CLB);
			setState(268);
			statements();
			setState(269);
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 10:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 20);
		case 1:
			return precpred(_ctx, 19);
		case 2:
			return precpred(_ctx, 18);
		case 3:
			return precpred(_ctx, 17);
		case 4:
			return precpred(_ctx, 16);
		case 5:
			return precpred(_ctx, 15);
		case 6:
			return precpred(_ctx, 14);
		case 7:
			return precpred(_ctx, 13);
		case 8:
			return precpred(_ctx, 12);
		case 9:
			return precpred(_ctx, 11);
		case 10:
			return precpred(_ctx, 10);
		case 11:
			return precpred(_ctx, 9);
		case 12:
			return precpred(_ctx, 8);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3-\u0112\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\5\2(\n\2\3\2\5\2+\n\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3\64\n\3"+
		"\3\3\5\3\67\n\3\3\3\3\3\5\3;\n\3\3\3\3\3\5\3?\n\3\3\3\3\3\3\4\3\4\3\4"+
		"\3\4\5\4G\n\4\3\4\3\4\5\4K\n\4\3\4\5\4N\n\4\3\4\3\4\5\4R\n\4\3\4\3\4\5"+
		"\4V\n\4\3\4\3\4\3\4\5\4[\n\4\3\5\5\5^\n\5\3\5\5\5a\n\5\3\5\5\5d\n\5\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6m\n\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3"+
		"\b\5\bx\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u0083\n\t\3\n\3\n"+
		"\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u0091\n\n\3\13\3\13\3\13"+
		"\3\13\3\13\3\13\3\13\5\13\u009a\n\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13"+
		"\3\13\5\13\u00a4\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f"+
		"\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00b8\n\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f"+
		"\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3"+
		"\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u00e1\n\f\f"+
		"\f\16\f\u00e4\13\f\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17\5\17\u00ef"+
		"\n\17\3\17\3\17\3\17\5\17\u00f4\n\17\3\17\3\17\5\17\u00f8\n\17\3\17\3"+
		"\17\5\17\u00fc\n\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u0105\n\17"+
		"\3\17\3\17\3\17\5\17\u010a\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\2\3"+
		"\26\21\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36\2\4\3\2\21\24\3\2\30\33"+
		"\2\u0132\2 \3\2\2\2\4.\3\2\2\2\6B\3\2\2\2\b]\3\2\2\2\nl\3\2\2\2\fn\3\2"+
		"\2\2\16w\3\2\2\2\20\u0082\3\2\2\2\22\u0090\3\2\2\2\24\u00a3\3\2\2\2\26"+
		"\u00b7\3\2\2\2\30\u00e5\3\2\2\2\32\u00e8\3\2\2\2\34\u0109\3\2\2\2\36\u010b"+
		"\3\2\2\2 !\7\37\2\2!\"\7#\2\2\"#\7 \2\2#$\7#\2\2$\'\5\4\3\2%&\7#\2\2&"+
		"(\5\6\4\2\'%\3\2\2\2\'(\3\2\2\2(*\3\2\2\2)+\7#\2\2*)\3\2\2\2*+\3\2\2\2"+
		"+,\3\2\2\2,-\7\2\2\3-\3\3\2\2\2./\7\36\2\2/\60\7!\2\2\60\61\7$\2\2\61"+
		"\63\7%\2\2\62\64\5\f\7\2\63\62\3\2\2\2\63\64\3\2\2\2\64\66\3\2\2\2\65"+
		"\67\7#\2\2\66\65\3\2\2\2\66\67\3\2\2\2\678\3\2\2\28:\7&\2\29;\7#\2\2:"+
		"9\3\2\2\2:;\3\2\2\2;<\3\2\2\2<>\5\b\5\2=?\7#\2\2>=\3\2\2\2>?\3\2\2\2?"+
		"@\3\2\2\2@A\7\'\2\2A\5\3\2\2\2BC\7\36\2\2CD\7,\2\2DF\7$\2\2EG\5\n\6\2"+
		"FE\3\2\2\2FG\3\2\2\2GH\3\2\2\2HJ\7%\2\2IK\5\f\7\2JI\3\2\2\2JK\3\2\2\2"+
		"KM\3\2\2\2LN\7#\2\2ML\3\2\2\2MN\3\2\2\2NO\3\2\2\2OQ\7&\2\2PR\7#\2\2QP"+
		"\3\2\2\2QR\3\2\2\2RS\3\2\2\2SU\5\b\5\2TV\7#\2\2UT\3\2\2\2UV\3\2\2\2VW"+
		"\3\2\2\2WZ\7\'\2\2XY\7#\2\2Y[\5\6\4\2ZX\3\2\2\2Z[\3\2\2\2[\7\3\2\2\2\\"+
		"^\5\16\b\2]\\\3\2\2\2]^\3\2\2\2^`\3\2\2\2_a\5\22\n\2`_\3\2\2\2`a\3\2\2"+
		"\2ac\3\2\2\2bd\5\30\r\2cb\3\2\2\2cd\3\2\2\2d\t\3\2\2\2ef\7,\2\2fm\5\f"+
		"\7\2gh\7,\2\2hi\5\f\7\2ij\7(\2\2jk\5\n\6\2km\3\2\2\2le\3\2\2\2lg\3\2\2"+
		"\2m\13\3\2\2\2no\t\2\2\2o\r\3\2\2\2pq\5\20\t\2qr\7#\2\2rx\3\2\2\2st\5"+
		"\20\t\2tu\7#\2\2uv\5\20\t\2vx\3\2\2\2wp\3\2\2\2ws\3\2\2\2x\17\3\2\2\2"+
		"yz\7\34\2\2z{\7,\2\2{|\5\f\7\2|}\7*\2\2}~\5\26\f\2~\u0083\3\2\2\2\177"+
		"\u0080\7,\2\2\u0080\u0081\7*\2\2\u0081\u0083\5\26\f\2\u0082y\3\2\2\2\u0082"+
		"\177\3\2\2\2\u0083\21\3\2\2\2\u0084\u0085\5\24\13\2\u0085\u0086\7#\2\2"+
		"\u0086\u0087\5\22\n\2\u0087\u0091\3\2\2\2\u0088\u0089\7&\2\2\u0089\u008a"+
		"\5\22\n\2\u008a\u008b\7\'\2\2\u008b\u008c\7#\2\2\u008c\u0091\3\2\2\2\u008d"+
		"\u008e\5\24\13\2\u008e\u008f\7#\2\2\u008f\u0091\3\2\2\2\u0090\u0084\3"+
		"\2\2\2\u0090\u0088\3\2\2\2\u0090\u008d\3\2\2\2\u0091\23\3\2\2\2\u0092"+
		"\u0093\7\34\2\2\u0093\u0094\7*\2\2\u0094\u00a4\5\26\f\2\u0095\u0096\7"+
		"\25\2\2\u0096\u0097\5\26\f\2\u0097\u0099\7&\2\2\u0098\u009a\7#\2\2\u0099"+
		"\u0098\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009c\5\b"+
		"\5\2\u009c\u009d\7\'\2\2\u009d\u00a4\3\2\2\2\u009e\u009f\7\"\2\2\u009f"+
		"\u00a0\7$\2\2\u00a0\u00a1\5\26\f\2\u00a1\u00a2\7%\2\2\u00a2\u00a4\3\2"+
		"\2\2\u00a3\u0092\3\2\2\2\u00a3\u0095\3\2\2\2\u00a3\u009e\3\2\2\2\u00a4"+
		"\25\3\2\2\2\u00a5\u00a6\b\f\1\2\u00a6\u00a7\7\20\2\2\u00a7\u00b8\5\26"+
		"\f\t\u00a8\u00a9\7\3\2\2\u00a9\u00b8\5\26\f\b\u00aa\u00ab\7\4\2\2\u00ab"+
		"\u00b8\5\26\f\7\u00ac\u00ad\7$\2\2\u00ad\u00ae\5\26\f\2\u00ae\u00af\7"+
		"%\2\2\u00af\u00b8\3\2\2\2\u00b0\u00b1\7,\2\2\u00b1\u00b2\7$\2\2\u00b2"+
		"\u00b3\5\26\f\2\u00b3\u00b4\7%\2\2\u00b4\u00b8\3\2\2\2\u00b5\u00b8\5\32"+
		"\16\2\u00b6\u00b8\7,\2\2\u00b7\u00a5\3\2\2\2\u00b7\u00a8\3\2\2\2\u00b7"+
		"\u00aa\3\2\2\2\u00b7\u00ac\3\2\2\2\u00b7\u00b0\3\2\2\2\u00b7\u00b5\3\2"+
		"\2\2\u00b7\u00b6\3\2\2\2\u00b8\u00e2\3\2\2\2\u00b9\u00ba\f\26\2\2\u00ba"+
		"\u00bb\7\17\2\2\u00bb\u00e1\5\26\f\27\u00bc\u00bd\f\25\2\2\u00bd\u00be"+
		"\7\16\2\2\u00be\u00e1\5\26\f\26\u00bf\u00c0\f\24\2\2\u00c0\u00c1\7\t\2"+
		"\2\u00c1\u00e1\5\26\f\25\u00c2\u00c3\f\23\2\2\u00c3\u00c4\7\b\2\2\u00c4"+
		"\u00e1\5\26\f\24\u00c5\u00c6\f\22\2\2\u00c6\u00c7\7\n\2\2\u00c7\u00e1"+
		"\5\26\f\23\u00c8\u00c9\f\21\2\2\u00c9\u00ca\7\13\2\2\u00ca\u00e1\5\26"+
		"\f\22\u00cb\u00cc\f\20\2\2\u00cc\u00cd\7\f\2\2\u00cd\u00e1\5\26\f\21\u00ce"+
		"\u00cf\f\17\2\2\u00cf\u00d0\7\r\2\2\u00d0\u00e1\5\26\f\20\u00d1\u00d2"+
		"\f\16\2\2\u00d2\u00d3\7\4\2\2\u00d3\u00e1\5\26\f\17\u00d4\u00d5\f\r\2"+
		"\2\u00d5\u00d6\7\3\2\2\u00d6\u00e1\5\26\f\16\u00d7\u00d8\f\f\2\2\u00d8"+
		"\u00d9\7\5\2\2\u00d9\u00e1\5\26\f\r\u00da\u00db\f\13\2\2\u00db\u00dc\7"+
		"\6\2\2\u00dc\u00e1\5\26\f\f\u00dd\u00de\f\n\2\2\u00de\u00df\7\7\2\2\u00df"+
		"\u00e1\5\26\f\13\u00e0\u00b9\3\2\2\2\u00e0\u00bc\3\2\2\2\u00e0\u00bf\3"+
		"\2\2\2\u00e0\u00c2\3\2\2\2\u00e0\u00c5\3\2\2\2\u00e0\u00c8\3\2\2\2\u00e0"+
		"\u00cb\3\2\2\2\u00e0\u00ce\3\2\2\2\u00e0\u00d1\3\2\2\2\u00e0\u00d4\3\2"+
		"\2\2\u00e0\u00d7\3\2\2\2\u00e0\u00da\3\2\2\2\u00e0\u00dd\3\2\2\2\u00e1"+
		"\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\27\3\2\2"+
		"\2\u00e4\u00e2\3\2\2\2\u00e5\u00e6\7\35\2\2\u00e6\u00e7\5\26\f\2\u00e7"+
		"\31\3\2\2\2\u00e8\u00e9\t\3\2\2\u00e9\33\3\2\2\2\u00ea\u00eb\7\25\2\2"+
		"\u00eb\u00ec\5\26\f\2\u00ec\u00ee\7&\2\2\u00ed\u00ef\7#\2\2\u00ee\u00ed"+
		"\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00f1\5\b\5\2\u00f1"+
		"\u00f3\7\'\2\2\u00f2\u00f4\7#\2\2\u00f3\u00f2\3\2\2\2\u00f3\u00f4\3\2"+
		"\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f7\7\26\2\2\u00f6\u00f8\7#\2\2\u00f7"+
		"\u00f6\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00fb\7&"+
		"\2\2\u00fa\u00fc\7#\2\2\u00fb\u00fa\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc"+
		"\u00fd\3\2\2\2\u00fd\u00fe\5\b\5\2\u00fe\u00ff\7\'\2\2\u00ff\u010a\3\2"+
		"\2\2\u0100\u0101\7\25\2\2\u0101\u0102\5\26\f\2\u0102\u0104\7&\2\2\u0103"+
		"\u0105\7#\2\2\u0104\u0103\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0106\3\2"+
		"\2\2\u0106\u0107\5\b\5\2\u0107\u0108\7\'\2\2\u0108\u010a\3\2\2\2\u0109"+
		"\u00ea\3\2\2\2\u0109\u0100\3\2\2\2\u010a\35\3\2\2\2\u010b\u010c\7\27\2"+
		"\2\u010c\u010d\5\26\f\2\u010d\u010e\7&\2\2\u010e\u010f\5\22\n\2\u010f"+
		"\u0110\7\'\2\2\u0110\37\3\2\2\2 \'*\63\66:>FJMQUZ]`clw\u0082\u0090\u0099"+
		"\u00a3\u00b7\u00e0\u00e2\u00ee\u00f3\u00f7\u00fb\u0104\u0109";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}