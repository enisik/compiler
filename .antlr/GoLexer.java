// Generated from /home/ensar/Documents/Compilerbau/compiler/GoLexer.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class GoLexer extends Lexer {
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
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"VAR", "RETURN", "FUNC", "PACKAGE", "IMPORT", "MAIN", "IF", "ELSE", "FOR", 
			"INT_TYPE", "FLOAT_TYPE", "BOOL_TYPE", "STRING_TYPE", "PLUS", "MINUS", 
			"STAR", "DIVISON", "MODULO", "EQUALS", "UNEQUAL", "LESS", "GREATER", 
			"LESSEQUAL", "GREATEREQUAL", "AND", "OR", "NOT", "INTEGER", "FLOAT", 
			"BOOL", "STRING", "NL", "LB", "RB", "CLB", "CRB", "COMMA", "DOT", "SEMICOLON", 
			"IS", "WHITESPACE", "COMMENT", "IDENTIFIER"
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


	public GoLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "GoLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2-\u0122\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3"+
		"\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7"+
		"\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13"+
		"\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3"+
		"\16\3\16\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3"+
		"\23\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3"+
		"\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\35\6\35\u00c5"+
		"\n\35\r\35\16\35\u00c6\3\36\6\36\u00ca\n\36\r\36\16\36\u00cb\3\36\3\36"+
		"\6\36\u00d0\n\36\r\36\16\36\u00d1\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3"+
		"\37\3\37\5\37\u00dd\n\37\3 \3 \6 \u00e1\n \r \16 \u00e2\3 \3 \3!\6!\u00e8"+
		"\n!\r!\16!\u00e9\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3"+
		"*\6*\u00fd\n*\r*\16*\u00fe\3*\3*\3+\3+\3+\3+\7+\u0107\n+\f+\16+\u010a"+
		"\13+\3+\3+\3+\3+\3+\7+\u0111\n+\f+\16+\u0114\13+\3+\3+\5+\u0118\n+\3+"+
		"\3+\3,\3,\7,\u011e\n,\f,\16,\u0121\13,\5\u00e2\u0108\u0112\2-\3\3\5\4"+
		"\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22"+
		"#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C"+
		"#E$G%I&K\'M(O)Q*S+U,W-\3\2\7\3\2\62;\4\2\f\f\17\17\4\2\13\13\"\"\4\2C"+
		"\\c|\6\2\62;C\\aac|\2\u012c\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3"+
		"\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2"+
		"\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37"+
		"\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3"+
		"\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2"+
		"\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C"+
		"\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2"+
		"\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\3Y\3\2\2\2\5]\3\2\2\2"+
		"\7d\3\2\2\2\ti\3\2\2\2\13q\3\2\2\2\rx\3\2\2\2\17}\3\2\2\2\21\u0080\3\2"+
		"\2\2\23\u0085\3\2\2\2\25\u0089\3\2\2\2\27\u008d\3\2\2\2\31\u0095\3\2\2"+
		"\2\33\u009a\3\2\2\2\35\u00a1\3\2\2\2\37\u00a3\3\2\2\2!\u00a5\3\2\2\2#"+
		"\u00a7\3\2\2\2%\u00a9\3\2\2\2\'\u00ab\3\2\2\2)\u00ae\3\2\2\2+\u00b1\3"+
		"\2\2\2-\u00b3\3\2\2\2/\u00b5\3\2\2\2\61\u00b8\3\2\2\2\63\u00bb\3\2\2\2"+
		"\65\u00be\3\2\2\2\67\u00c1\3\2\2\29\u00c4\3\2\2\2;\u00c9\3\2\2\2=\u00dc"+
		"\3\2\2\2?\u00de\3\2\2\2A\u00e7\3\2\2\2C\u00eb\3\2\2\2E\u00ed\3\2\2\2G"+
		"\u00ef\3\2\2\2I\u00f1\3\2\2\2K\u00f3\3\2\2\2M\u00f5\3\2\2\2O\u00f7\3\2"+
		"\2\2Q\u00f9\3\2\2\2S\u00fc\3\2\2\2U\u0117\3\2\2\2W\u011b\3\2\2\2YZ\7x"+
		"\2\2Z[\7c\2\2[\\\7t\2\2\\\4\3\2\2\2]^\7t\2\2^_\7g\2\2_`\7v\2\2`a\7w\2"+
		"\2ab\7t\2\2bc\7p\2\2c\6\3\2\2\2de\7h\2\2ef\7w\2\2fg\7p\2\2gh\7e\2\2h\b"+
		"\3\2\2\2ij\7r\2\2jk\7c\2\2kl\7e\2\2lm\7m\2\2mn\7c\2\2no\7i\2\2op\7g\2"+
		"\2p\n\3\2\2\2qr\7k\2\2rs\7o\2\2st\7r\2\2tu\7q\2\2uv\7t\2\2vw\7v\2\2w\f"+
		"\3\2\2\2xy\7o\2\2yz\7c\2\2z{\7k\2\2{|\7p\2\2|\16\3\2\2\2}~\7k\2\2~\177"+
		"\7h\2\2\177\20\3\2\2\2\u0080\u0081\7g\2\2\u0081\u0082\7n\2\2\u0082\u0083"+
		"\7u\2\2\u0083\u0084\7g\2\2\u0084\22\3\2\2\2\u0085\u0086\7h\2\2\u0086\u0087"+
		"\7q\2\2\u0087\u0088\7t\2\2\u0088\24\3\2\2\2\u0089\u008a\7k\2\2\u008a\u008b"+
		"\7p\2\2\u008b\u008c\7v\2\2\u008c\26\3\2\2\2\u008d\u008e\7h\2\2\u008e\u008f"+
		"\7n\2\2\u008f\u0090\7q\2\2\u0090\u0091\7c\2\2\u0091\u0092\7v\2\2\u0092"+
		"\u0093\78\2\2\u0093\u0094\7\66\2\2\u0094\30\3\2\2\2\u0095\u0096\7d\2\2"+
		"\u0096\u0097\7q\2\2\u0097\u0098\7q\2\2\u0098\u0099\7n\2\2\u0099\32\3\2"+
		"\2\2\u009a\u009b\7u\2\2\u009b\u009c\7v\2\2\u009c\u009d\7t\2\2\u009d\u009e"+
		"\7k\2\2\u009e\u009f\7p\2\2\u009f\u00a0\7i\2\2\u00a0\34\3\2\2\2\u00a1\u00a2"+
		"\7-\2\2\u00a2\36\3\2\2\2\u00a3\u00a4\7/\2\2\u00a4 \3\2\2\2\u00a5\u00a6"+
		"\7,\2\2\u00a6\"\3\2\2\2\u00a7\u00a8\7\61\2\2\u00a8$\3\2\2\2\u00a9\u00aa"+
		"\7\'\2\2\u00aa&\3\2\2\2\u00ab\u00ac\7?\2\2\u00ac\u00ad\7?\2\2\u00ad(\3"+
		"\2\2\2\u00ae\u00af\7#\2\2\u00af\u00b0\7?\2\2\u00b0*\3\2\2\2\u00b1\u00b2"+
		"\7>\2\2\u00b2,\3\2\2\2\u00b3\u00b4\7@\2\2\u00b4.\3\2\2\2\u00b5\u00b6\7"+
		">\2\2\u00b6\u00b7\7?\2\2\u00b7\60\3\2\2\2\u00b8\u00b9\7@\2\2\u00b9\u00ba"+
		"\7?\2\2\u00ba\62\3\2\2\2\u00bb\u00bc\7(\2\2\u00bc\u00bd\7(\2\2\u00bd\64"+
		"\3\2\2\2\u00be\u00bf\7~\2\2\u00bf\u00c0\7~\2\2\u00c0\66\3\2\2\2\u00c1"+
		"\u00c2\7#\2\2\u00c28\3\2\2\2\u00c3\u00c5\t\2\2\2\u00c4\u00c3\3\2\2\2\u00c5"+
		"\u00c6\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7:\3\2\2\2"+
		"\u00c8\u00ca\t\2\2\2\u00c9\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00c9"+
		"\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00cf\7\60\2\2"+
		"\u00ce\u00d0\t\2\2\2\u00cf\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00cf"+
		"\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2<\3\2\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5"+
		"\7t\2\2\u00d5\u00d6\7w\2\2\u00d6\u00dd\7g\2\2\u00d7\u00d8\7h\2\2\u00d8"+
		"\u00d9\7c\2\2\u00d9\u00da\7n\2\2\u00da\u00db\7u\2\2\u00db\u00dd\7g\2\2"+
		"\u00dc\u00d3\3\2\2\2\u00dc\u00d7\3\2\2\2\u00dd>\3\2\2\2\u00de\u00e0\7"+
		"$\2\2\u00df\u00e1\13\2\2\2\u00e0\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2"+
		"\u00e3\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5\7$"+
		"\2\2\u00e5@\3\2\2\2\u00e6\u00e8\t\3\2\2\u00e7\u00e6\3\2\2\2\u00e8\u00e9"+
		"\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00eaB\3\2\2\2\u00eb"+
		"\u00ec\7*\2\2\u00ecD\3\2\2\2\u00ed\u00ee\7+\2\2\u00eeF\3\2\2\2\u00ef\u00f0"+
		"\7}\2\2\u00f0H\3\2\2\2\u00f1\u00f2\7\177\2\2\u00f2J\3\2\2\2\u00f3\u00f4"+
		"\7.\2\2\u00f4L\3\2\2\2\u00f5\u00f6\7\60\2\2\u00f6N\3\2\2\2\u00f7\u00f8"+
		"\7=\2\2\u00f8P\3\2\2\2\u00f9\u00fa\7?\2\2\u00faR\3\2\2\2\u00fb\u00fd\t"+
		"\4\2\2\u00fc\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe"+
		"\u00ff\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0101\b*\2\2\u0101T\3\2\2\2\u0102"+
		"\u0103\7\61\2\2\u0103\u0104\7\61\2\2\u0104\u0108\3\2\2\2\u0105\u0107\13"+
		"\2\2\2\u0106\u0105\3\2\2\2\u0107\u010a\3\2\2\2\u0108\u0109\3\2\2\2\u0108"+
		"\u0106\3\2\2\2\u0109\u010b\3\2\2\2\u010a\u0108\3\2\2\2\u010b\u0118\7\f"+
		"\2\2\u010c\u010d\7\61\2\2\u010d\u010e\7,\2\2\u010e\u0112\3\2\2\2\u010f"+
		"\u0111\13\2\2\2\u0110\u010f\3\2\2\2\u0111\u0114\3\2\2\2\u0112\u0113\3"+
		"\2\2\2\u0112\u0110\3\2\2\2\u0113\u0115\3\2\2\2\u0114\u0112\3\2\2\2\u0115"+
		"\u0116\7,\2\2\u0116\u0118\7\61\2\2\u0117\u0102\3\2\2\2\u0117\u010c\3\2"+
		"\2\2\u0118\u0119\3\2\2\2\u0119\u011a\b+\2\2\u011aV\3\2\2\2\u011b\u011f"+
		"\t\5\2\2\u011c\u011e\t\6\2\2\u011d\u011c\3\2\2\2\u011e\u0121\3\2\2\2\u011f"+
		"\u011d\3\2\2\2\u011f\u0120\3\2\2\2\u0120X\3\2\2\2\u0121\u011f\3\2\2\2"+
		"\16\2\u00c6\u00cb\u00d1\u00dc\u00e2\u00e9\u00fe\u0108\u0112\u0117\u011f"+
		"\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}