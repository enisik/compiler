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
		FLOAT_TYPE=16, BOOL_TYPE=17, STRING_TYPE=18, VAR_TYPE=19, IF=20, ELSE=21, 
		FOR=22, INTEGER=23, FLOAT=24, BOOL=25, STRING=26, FUNC=27, PACKAGE=28, 
		IMPORT=29, MAIN=30, NEWLINE=31, LB=32, RB=33, CLB=34, CRB=35, IDENTIFIER=36, 
		COMMENT=37;
	public static final int
		RULE_prog = 0, RULE_main_method = 1, RULE_methods = 2, RULE_func_body = 3, 
		RULE_func_args = 4, RULE_return_type = 5;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "main_method", "methods", "func_body", "func_args", "return_type"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'>'", 
			"'<='", "'>='", "'&&'", "'||'", "'!'", "'int'", "'float'", "'bool'", 
			"'string'", "'var'", "'if'", "'else'", "'for'", null, null, null, null, 
			"'func'", "'package main'", "'import \"fmt\"'", "'main'", null, "'('", 
			"')'", "'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PLUS", "MINUS", "STAR", "DIVISON", "MODULO", "EQUALS", "UNEQUAL", 
			"LESS", "GREATER", "LESSEQUAL", "GREATEREQUAL", "AND", "OR", "NOT", "INT_TYPE", 
			"FLOAT_TYPE", "BOOL_TYPE", "STRING_TYPE", "VAR_TYPE", "IF", "ELSE", "FOR", 
			"INTEGER", "FLOAT", "BOOL", "STRING", "FUNC", "PACKAGE", "IMPORT", "MAIN", 
			"NEWLINE", "LB", "RB", "CLB", "CRB", "IDENTIFIER", "COMMENT"
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

	public static class ProgContext extends ParserRuleContext {
		public TerminalNode PACKAGE() { return getToken(GoParser.PACKAGE, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(GoParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(GoParser.NEWLINE, i);
		}
		public TerminalNode IMPORT() { return getToken(GoParser.IMPORT, 0); }
		public Main_methodContext main_method() {
			return getRuleContext(Main_methodContext.class,0);
		}
		public MethodsContext methods() {
			return getRuleContext(MethodsContext.class,0);
		}
		public TerminalNode EOF() { return getToken(GoParser.EOF, 0); }
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(12);
			match(PACKAGE);
			setState(13);
			match(NEWLINE);
			setState(14);
			match(NEWLINE);
			setState(15);
			match(IMPORT);
			setState(16);
			main_method();
			setState(17);
			methods();
			setState(18);
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
		public TerminalNode INT_TYPE() { return getToken(GoParser.INT_TYPE, 0); }
		public TerminalNode CLB() { return getToken(GoParser.CLB, 0); }
		public Func_bodyContext func_body() {
			return getRuleContext(Func_bodyContext.class,0);
		}
		public TerminalNode CRB() { return getToken(GoParser.CRB, 0); }
		public MethodsContext methods() {
			return getRuleContext(MethodsContext.class,0);
		}
		public Main_methodContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main_method; }
	}

	public final Main_methodContext main_method() throws RecognitionException {
		Main_methodContext _localctx = new Main_methodContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_main_method);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(20);
			match(FUNC);
			setState(21);
			match(MAIN);
			setState(22);
			match(LB);
			setState(23);
			match(RB);
			setState(24);
			match(INT_TYPE);
			setState(25);
			match(CLB);
			setState(26);
			func_body();
			setState(27);
			match(CRB);
			setState(28);
			methods();
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
		public Func_argsContext func_args() {
			return getRuleContext(Func_argsContext.class,0);
		}
		public TerminalNode RB() { return getToken(GoParser.RB, 0); }
		public Return_typeContext return_type() {
			return getRuleContext(Return_typeContext.class,0);
		}
		public TerminalNode CLB() { return getToken(GoParser.CLB, 0); }
		public Func_bodyContext func_body() {
			return getRuleContext(Func_bodyContext.class,0);
		}
		public TerminalNode CRB() { return getToken(GoParser.CRB, 0); }
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
			setState(30);
			match(FUNC);
			setState(31);
			match(IDENTIFIER);
			setState(32);
			match(LB);
			setState(33);
			func_args();
			setState(34);
			match(RB);
			setState(35);
			return_type();
			setState(36);
			match(CLB);
			setState(37);
			func_body();
			setState(38);
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

	public static class Func_bodyContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(GoParser.IDENTIFIER, 0); }
		public Func_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_body; }
	}

	public final Func_bodyContext func_body() throws RecognitionException {
		Func_bodyContext _localctx = new Func_bodyContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_func_body);
		try {
			setState(42);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(40);
				match(IDENTIFIER);
				}
				break;
			case CRB:
				enterOuterAlt(_localctx, 2);
				{
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

	public static class Func_argsContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(GoParser.IDENTIFIER, 0); }
		public Func_argsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_args; }
	}

	public final Func_argsContext func_args() throws RecognitionException {
		Func_argsContext _localctx = new Func_argsContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_func_args);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(44);
			match(IDENTIFIER);
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

	public static class Return_typeContext extends ParserRuleContext {
		public TerminalNode INT_TYPE() { return getToken(GoParser.INT_TYPE, 0); }
		public TerminalNode BOOL_TYPE() { return getToken(GoParser.BOOL_TYPE, 0); }
		public TerminalNode FLOAT_TYPE() { return getToken(GoParser.FLOAT_TYPE, 0); }
		public TerminalNode STRING_TYPE() { return getToken(GoParser.STRING_TYPE, 0); }
		public Return_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_type; }
	}

	public final Return_typeContext return_type() throws RecognitionException {
		Return_typeContext _localctx = new Return_typeContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_return_type);
		try {
			setState(51);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT_TYPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(46);
				match(INT_TYPE);
				}
				break;
			case BOOL_TYPE:
				enterOuterAlt(_localctx, 2);
				{
				setState(47);
				match(BOOL_TYPE);
				}
				break;
			case FLOAT_TYPE:
				enterOuterAlt(_localctx, 3);
				{
				setState(48);
				match(FLOAT_TYPE);
				}
				break;
			case STRING_TYPE:
				enterOuterAlt(_localctx, 4);
				{
				setState(49);
				match(STRING_TYPE);
				}
				break;
			case CLB:
				enterOuterAlt(_localctx, 5);
				{
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\'8\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3"+
		"\4\3\4\3\5\3\5\5\5-\n\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\5\7\66\n\7\3\7\2\2"+
		"\b\2\4\6\b\n\f\2\2\2\66\2\16\3\2\2\2\4\26\3\2\2\2\6 \3\2\2\2\b,\3\2\2"+
		"\2\n.\3\2\2\2\f\65\3\2\2\2\16\17\7\36\2\2\17\20\7!\2\2\20\21\7!\2\2\21"+
		"\22\7\37\2\2\22\23\5\4\3\2\23\24\5\6\4\2\24\25\7\2\2\3\25\3\3\2\2\2\26"+
		"\27\7\35\2\2\27\30\7 \2\2\30\31\7\"\2\2\31\32\7#\2\2\32\33\7\21\2\2\33"+
		"\34\7$\2\2\34\35\5\b\5\2\35\36\7%\2\2\36\37\5\6\4\2\37\5\3\2\2\2 !\7\35"+
		"\2\2!\"\7&\2\2\"#\7\"\2\2#$\5\n\6\2$%\7#\2\2%&\5\f\7\2&\'\7$\2\2\'(\5"+
		"\b\5\2()\7%\2\2)\7\3\2\2\2*-\7&\2\2+-\3\2\2\2,*\3\2\2\2,+\3\2\2\2-\t\3"+
		"\2\2\2./\7&\2\2/\13\3\2\2\2\60\66\7\21\2\2\61\66\7\23\2\2\62\66\7\22\2"+
		"\2\63\66\7\24\2\2\64\66\3\2\2\2\65\60\3\2\2\2\65\61\3\2\2\2\65\62\3\2"+
		"\2\2\65\63\3\2\2\2\65\64\3\2\2\2\66\r\3\2\2\2\4,\65";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}