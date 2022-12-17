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
		VAR=1, RETURN=2, FUNC=3, PACKAGE=4, IMPORT=5, IF=6, ELSE=7, FOR=8, INT_TYPE=9, 
		FLOAT_TYPE=10, BOOL_TYPE=11, STRING_TYPE=12, PLUS=13, MINUS=14, STAR=15, 
		DIVISON=16, MODULO=17, EQUALS=18, UNEQUAL=19, LESS=20, GREATER=21, LESSEQUAL=22, 
		GREATEREQUAL=23, AND=24, OR=25, NOT=26, INTEGER=27, FLOAT=28, BOOL=29, 
		STRING=30, NL=31, LB=32, RB=33, CLB=34, CRB=35, COMMA=36, DOT=37, SEMICOLON=38, 
		ASSIGN=39, WHITESPACE=40, COMMENT=41, IDENTIFIER=42;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"VAR", "RETURN", "FUNC", "PACKAGE", "IMPORT", "IF", "ELSE", "FOR", "INT_TYPE", 
			"FLOAT_TYPE", "BOOL_TYPE", "STRING_TYPE", "PLUS", "MINUS", "STAR", "DIVISON", 
			"MODULO", "EQUALS", "UNEQUAL", "LESS", "GREATER", "LESSEQUAL", "GREATEREQUAL", 
			"AND", "OR", "NOT", "INTEGER", "FLOAT", "BOOL", "STRING", "NL", "LB", 
			"RB", "CLB", "CRB", "COMMA", "DOT", "SEMICOLON", "ASSIGN", "WHITESPACE", 
			"COMMENT", "IDENTIFIER"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2,\u0122\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3"+
		"\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5"+
		"\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3"+
		"\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13"+
		"\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3"+
		"\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3"+
		"\24\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3"+
		"\32\3\32\3\32\3\33\3\33\3\34\6\34\u00be\n\34\r\34\16\34\u00bf\3\35\6\35"+
		"\u00c3\n\35\r\35\16\35\u00c4\3\35\3\35\6\35\u00c9\n\35\r\35\16\35\u00ca"+
		"\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u00d6\n\36\3\37\3\37"+
		"\6\37\u00da\n\37\r\37\16\37\u00db\3\37\3\37\3\37\5\37\u00e1\n\37\3 \6"+
		" \u00e4\n \r \16 \u00e5\3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'"+
		"\3(\3(\3)\6)\u00f9\n)\r)\16)\u00fa\3)\3)\3*\3*\3*\3*\7*\u0103\n*\f*\16"+
		"*\u0106\13*\3*\3*\3*\3*\3*\7*\u010d\n*\f*\16*\u0110\13*\3*\3*\3*\3*\5"+
		"*\u0116\n*\5*\u0118\n*\3*\3*\3+\3+\7+\u011e\n+\f+\16+\u0121\13+\5\u00db"+
		"\u0104\u010e\2,\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31"+
		"\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65"+
		"\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,\3\2\7\3\2\62;\4\2\f\f\17"+
		"\17\4\2\13\13\"\"\4\2C\\c|\6\2\62;C\\aac|\2\u012e\2\3\3\2\2\2\2\5\3\2"+
		"\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21"+
		"\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2"+
		"\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3"+
		"\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3"+
		"\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3"+
		"\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2"+
		"\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\3W\3\2\2\2\5"+
		"[\3\2\2\2\7b\3\2\2\2\tg\3\2\2\2\13o\3\2\2\2\rv\3\2\2\2\17y\3\2\2\2\21"+
		"~\3\2\2\2\23\u0082\3\2\2\2\25\u0086\3\2\2\2\27\u008e\3\2\2\2\31\u0093"+
		"\3\2\2\2\33\u009a\3\2\2\2\35\u009c\3\2\2\2\37\u009e\3\2\2\2!\u00a0\3\2"+
		"\2\2#\u00a2\3\2\2\2%\u00a4\3\2\2\2\'\u00a7\3\2\2\2)\u00aa\3\2\2\2+\u00ac"+
		"\3\2\2\2-\u00ae\3\2\2\2/\u00b1\3\2\2\2\61\u00b4\3\2\2\2\63\u00b7\3\2\2"+
		"\2\65\u00ba\3\2\2\2\67\u00bd\3\2\2\29\u00c2\3\2\2\2;\u00d5\3\2\2\2=\u00e0"+
		"\3\2\2\2?\u00e3\3\2\2\2A\u00e7\3\2\2\2C\u00e9\3\2\2\2E\u00eb\3\2\2\2G"+
		"\u00ed\3\2\2\2I\u00ef\3\2\2\2K\u00f1\3\2\2\2M\u00f3\3\2\2\2O\u00f5\3\2"+
		"\2\2Q\u00f8\3\2\2\2S\u0117\3\2\2\2U\u011b\3\2\2\2WX\7x\2\2XY\7c\2\2YZ"+
		"\7t\2\2Z\4\3\2\2\2[\\\7t\2\2\\]\7g\2\2]^\7v\2\2^_\7w\2\2_`\7t\2\2`a\7"+
		"p\2\2a\6\3\2\2\2bc\7h\2\2cd\7w\2\2de\7p\2\2ef\7e\2\2f\b\3\2\2\2gh\7r\2"+
		"\2hi\7c\2\2ij\7e\2\2jk\7m\2\2kl\7c\2\2lm\7i\2\2mn\7g\2\2n\n\3\2\2\2op"+
		"\7k\2\2pq\7o\2\2qr\7r\2\2rs\7q\2\2st\7t\2\2tu\7v\2\2u\f\3\2\2\2vw\7k\2"+
		"\2wx\7h\2\2x\16\3\2\2\2yz\7g\2\2z{\7n\2\2{|\7u\2\2|}\7g\2\2}\20\3\2\2"+
		"\2~\177\7h\2\2\177\u0080\7q\2\2\u0080\u0081\7t\2\2\u0081\22\3\2\2\2\u0082"+
		"\u0083\7k\2\2\u0083\u0084\7p\2\2\u0084\u0085\7v\2\2\u0085\24\3\2\2\2\u0086"+
		"\u0087\7h\2\2\u0087\u0088\7n\2\2\u0088\u0089\7q\2\2\u0089\u008a\7c\2\2"+
		"\u008a\u008b\7v\2\2\u008b\u008c\78\2\2\u008c\u008d\7\66\2\2\u008d\26\3"+
		"\2\2\2\u008e\u008f\7d\2\2\u008f\u0090\7q\2\2\u0090\u0091\7q\2\2\u0091"+
		"\u0092\7n\2\2\u0092\30\3\2\2\2\u0093\u0094\7u\2\2\u0094\u0095\7v\2\2\u0095"+
		"\u0096\7t\2\2\u0096\u0097\7k\2\2\u0097\u0098\7p\2\2\u0098\u0099\7i\2\2"+
		"\u0099\32\3\2\2\2\u009a\u009b\7-\2\2\u009b\34\3\2\2\2\u009c\u009d\7/\2"+
		"\2\u009d\36\3\2\2\2\u009e\u009f\7,\2\2\u009f \3\2\2\2\u00a0\u00a1\7\61"+
		"\2\2\u00a1\"\3\2\2\2\u00a2\u00a3\7\'\2\2\u00a3$\3\2\2\2\u00a4\u00a5\7"+
		"?\2\2\u00a5\u00a6\7?\2\2\u00a6&\3\2\2\2\u00a7\u00a8\7#\2\2\u00a8\u00a9"+
		"\7?\2\2\u00a9(\3\2\2\2\u00aa\u00ab\7>\2\2\u00ab*\3\2\2\2\u00ac\u00ad\7"+
		"@\2\2\u00ad,\3\2\2\2\u00ae\u00af\7>\2\2\u00af\u00b0\7?\2\2\u00b0.\3\2"+
		"\2\2\u00b1\u00b2\7@\2\2\u00b2\u00b3\7?\2\2\u00b3\60\3\2\2\2\u00b4\u00b5"+
		"\7(\2\2\u00b5\u00b6\7(\2\2\u00b6\62\3\2\2\2\u00b7\u00b8\7~\2\2\u00b8\u00b9"+
		"\7~\2\2\u00b9\64\3\2\2\2\u00ba\u00bb\7#\2\2\u00bb\66\3\2\2\2\u00bc\u00be"+
		"\t\2\2\2\u00bd\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00bd\3\2\2\2\u00bf"+
		"\u00c0\3\2\2\2\u00c08\3\2\2\2\u00c1\u00c3\t\2\2\2\u00c2\u00c1\3\2\2\2"+
		"\u00c3\u00c4\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6"+
		"\3\2\2\2\u00c6\u00c8\7\60\2\2\u00c7\u00c9\t\2\2\2\u00c8\u00c7\3\2\2\2"+
		"\u00c9\u00ca\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb:\3"+
		"\2\2\2\u00cc\u00cd\7v\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf\7w\2\2\u00cf"+
		"\u00d6\7g\2\2\u00d0\u00d1\7h\2\2\u00d1\u00d2\7c\2\2\u00d2\u00d3\7n\2\2"+
		"\u00d3\u00d4\7u\2\2\u00d4\u00d6\7g\2\2\u00d5\u00cc\3\2\2\2\u00d5\u00d0"+
		"\3\2\2\2\u00d6<\3\2\2\2\u00d7\u00d9\7$\2\2\u00d8\u00da\13\2\2\2\u00d9"+
		"\u00d8\3\2\2\2\u00da\u00db\3\2\2\2\u00db\u00dc\3\2\2\2\u00db\u00d9\3\2"+
		"\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00e1\7$\2\2\u00de\u00df\7$\2\2\u00df\u00e1"+
		"\7$\2\2\u00e0\u00d7\3\2\2\2\u00e0\u00de\3\2\2\2\u00e1>\3\2\2\2\u00e2\u00e4"+
		"\t\3\2\2\u00e3\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5"+
		"\u00e6\3\2\2\2\u00e6@\3\2\2\2\u00e7\u00e8\7*\2\2\u00e8B\3\2\2\2\u00e9"+
		"\u00ea\7+\2\2\u00eaD\3\2\2\2\u00eb\u00ec\7}\2\2\u00ecF\3\2\2\2\u00ed\u00ee"+
		"\7\177\2\2\u00eeH\3\2\2\2\u00ef\u00f0\7.\2\2\u00f0J\3\2\2\2\u00f1\u00f2"+
		"\7\60\2\2\u00f2L\3\2\2\2\u00f3\u00f4\7=\2\2\u00f4N\3\2\2\2\u00f5\u00f6"+
		"\7?\2\2\u00f6P\3\2\2\2\u00f7\u00f9\t\4\2\2\u00f8\u00f7\3\2\2\2\u00f9\u00fa"+
		"\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc"+
		"\u00fd\b)\2\2\u00fdR\3\2\2\2\u00fe\u00ff\7\61\2\2\u00ff\u0100\7\61\2\2"+
		"\u0100\u0104\3\2\2\2\u0101\u0103\13\2\2\2\u0102\u0101\3\2\2\2\u0103\u0106"+
		"\3\2\2\2\u0104\u0105\3\2\2\2\u0104\u0102\3\2\2\2\u0105\u0107\3\2\2\2\u0106"+
		"\u0104\3\2\2\2\u0107\u0118\7\f\2\2\u0108\u0109\7\61\2\2\u0109\u010a\7"+
		",\2\2\u010a\u010e\3\2\2\2\u010b\u010d\13\2\2\2\u010c\u010b\3\2\2\2\u010d"+
		"\u0110\3\2\2\2\u010e\u010f\3\2\2\2\u010e\u010c\3\2\2\2\u010f\u0111\3\2"+
		"\2\2\u0110\u010e\3\2\2\2\u0111\u0112\7,\2\2\u0112\u0113\7\61\2\2\u0113"+
		"\u0115\3\2\2\2\u0114\u0116\5? \2\u0115\u0114\3\2\2\2\u0115\u0116\3\2\2"+
		"\2\u0116\u0118\3\2\2\2\u0117\u00fe\3\2\2\2\u0117\u0108\3\2\2\2\u0118\u0119"+
		"\3\2\2\2\u0119\u011a\b*\2\2\u011aT\3\2\2\2\u011b\u011f\t\5\2\2\u011c\u011e"+
		"\t\6\2\2\u011d\u011c\3\2\2\2\u011e\u0121\3\2\2\2\u011f\u011d\3\2\2\2\u011f"+
		"\u0120\3\2\2\2\u0120V\3\2\2\2\u0121\u011f\3\2\2\2\20\2\u00bf\u00c4\u00ca"+
		"\u00d5\u00db\u00e0\u00e5\u00fa\u0104\u010e\u0115\u0117\u011f\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}