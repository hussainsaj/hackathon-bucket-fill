from app import strokesRequired
import unittest

class TestStrokesRequired(unittest.TestCase):
    def testInput000(self):
        actual = strokesRequired(
            ['aaaba',
            'ababa',
            'aaaca']
        )
        expected = 5
        self.assertEqual(actual, expected)

    def testInput001(self):
        actual = strokesRequired(
            ['bbba',
            'abba',
            'acaa',
            'aaac']
        )
        expected = 4
        self.assertEqual(actual, expected)

    def testInput002(self):
        actual = strokesRequired(
            ['abbcaccbb']
        )
        expected = 6
        self.assertEqual(actual, expected)

    def testInput003(self):
        actual = strokesRequired(
            ['aaabbbccbaaaacbbabbb',
            'caaabaaaaaabbbbaaaaa',
            'aaaaaabbbaacabaaaaab',
            'caaaabaaaabbaabbaaab',
            'ababbaaaaaabbbababba',
            'aaaacbbabacbcaaaacac',
            'abacbcbcabbbacaaabaa',
            'bbbcabbbbacacabbbaba',
            'babbabbaababcacccbbb',
            'abbbaabcbbabbaabaaaa',
            'babaacbbaabaabababab',
            'aaabbaabaacbbbbababb',
            'caabacabcbbcabacbaac',
            'bbcbcaabbcbaabbababb',
            'baabacaabbbaabbaabaa',
            'cabbbaabbabaabaaaacb',
            'aabbbcbabbbaaaaabbab',
            'bbaaabacbbbabbabacac',
            'baaacbaacbabcbbbabab',
            'acabbbcabcbcabaacabc']
        )
        expected = 129
        self.assertEqual(actual, expected)

    def testInput004(self):
        actual = strokesRequired(
            ['cbbabbabacabacbabbbbca',
            'baababccbcbaaaacacaaac',
            'abcbaabaaaabbabccababa',
            'abaaabccacaabcabaaaabb',
            'aabbccaababbaaabbbbcbc',
            'aabaaaaaabaaacaaaabaaa',
            'aacbbbbabaaaababcbbacb',
            'acaacaaababbbbbabaabaa',
            'bbbabbabbbccbaaaaabaab',
            'bbbaabbaaaacabacaababb',
            'baaaabbacabacbbbabaaba',
            'babaaacbabaacbaaababca',
            'bacabbacbabaabaaccbcaa',
            'baabaaaaaaaaaaabbabbaa',
            'aabaacaaaabbbbbacabaaa',
            'aabbaaaabaabaabbaabaaa',
            'bbacbcacacaaaaaabbbabc']
        )
        expected = 119
        self.assertEqual(actual, expected)

    def testInput005(self):
        actual = strokesRequired(
            ['babcaabccbabbbccbabaabcbaba',
            'cccaacbbababaccacaacbbaaaaa',
            'aabbcbaabaaaaacaaaaacaaabba',
            'abaaacaabacaccccaaaaaccaaaa',
            'aacacacaaacbaabbbacababacbb',
            'acbabbcaabbcccaacaacaabcbba',
            'abcacaaaaaaaabcbcbaaaaacaba',
            'aaacccbbabaccabaacabaabcaaa',
            'aabacbcaaababcacbaaaacbacac',
            'bbbbaaacbaaaccccbcacbcbacaa',
            'caabaacccacaaabbaaacabaacac',
            'aabcbaaacabbacbacabaabacbbc',
            'aaabacbaaccbaaabccbcaaaacab',
            'aaaaaaaacbaabcabbabcaaabbbc',
            'cabbbaacccaaaacbaabaaabaaaa',
            'bbbbaaabacacbbaaaccbaaaaaba',
            'caacaaaaacbabcabbaccbccaaac',
            'acbaaaccaccbaacccacaaaabaab',
            'bbccaabaaaababcabbaabccacac',
            'bacaaaababcaacaacacbbaaacca',
            'ccaaaaababaacacbaaaabaaaaab',
            'acabcacaaabaacacacbcbbaacba',
            'abccccacaaaabaaaaccbaabaabb',
            'cacbcaabbbbaaaacbccababcbaa',
            'abaaabaaababbbaaaaababaaaaa',
            'aababbcbcaaacbbaaaaaaaaacaa',
            'bcacaaccaaacbaaabbbaaaaaaba',
            'acaacaaacbbbacbaaaabbaccacc',
            'ccbcaccabcacaacccacaaabbaaa',
            'caaabacacabbbababbcbcaaaaca',
            'acbacacabbababaacaacabacaba',
            'cbaccbaaaaaaabaabaccaabccaa',
            'bcacacbaaaaccacbbabaabcabca',
            'aabccbbcabaababaaaaaaaaaabc',
            'acaabacabaaabbcacaacabbcabb',
            'aacbaabaaaaabcaaabccaaaabba',
            'aabaaccabcaacbbbcbcccbaccba',
            'cbaabbababaacbbabbabcaaacab',
            'cabbccacabbbaaacacaaabcaaaa',
            'cacababbcbbcbcbbacbaabacbaa',
            'aacabaaaabbbbbbababaabaaaab',
            'caabccaacbaacbbacbbcbabaaaa',
            'caccabcbbcaccaccbbbccbcaabc',
            'aaaaaacabaccaabcaaacaaacacc',
            'cacabacbcaabaababcbbabcacba',
            'babaacabaccacbbaacaaaaaaaab',
            'bcbcaaaaccaacaaaccaaaacbbac',
            'abacacbaacaacaacaaabaabcaca',
            'ccaaaacbbbbcabcbbcbcaacabaa',
            'caaacaacccbbcbabbbabbaacabc',
            'bbabcaacbabacaaaaaabaacabba',
            'aabbaaaabbbaaaaaaabbaacaaab',
            'caccbabacccaccacabcbbabcaba',
            'aacccaabcacaababcabacbacbaa',
            'aaabbcababaabaacbcacaaacbaa',
            'cabaaaaaaacabacabccccbcbbbb',
            'ccabcaabbacbcbaabcbaabbcacc',
            'aabbbbcbacbabcbabcacabacbca',
            'aacabacaabacbacaaaaabbaccaa',
            'ccbbbaaababcaaaabaabbaabacc',
            'ccbabacaababaacbbaacbacabca',
            'baaacacaabbaaccbccaacbaaaaa',
            'bccaacacababbccaaacabcaaaaa',
            'caaabcacaaabacabbbababcaabc',
            'bacacccaabcbaaaaaaabacaaaba',
            'aaaaccacabaccacaabaacbaabcc',
            'cbbabacabcbacbbbaaacabaaaaa',
            'aacabaacaaaacbcbabcaacacaca',
            'aacbacaaacaaaacaabbaaabcbac',
            'babaaacacaabaaacaababaabcac',
            'bbbaaaababaccaacabaaacaccab',
            'abbaaaaacbaccacbaabacabaccb',
            'bbbaabaabcbaaaccaaababbcbab',
            'abcaaacabccacaaccacbcccaaaa',
            'aaaaaccabcaaccaacaaababccca',
            'acbcabaabcbbcaaaacbaaccbaab',
            'cacccbcabaaaccaaaacbccbbabb',
            'cababbbaaabaabacbaaabccbaab',
            'caacbcaaaaababaabaabaaacaac',
            'abaaaaacacaaabccabaabcaaaca',
            'aacaaaaaaaaaabbaccbacbaaacb',
            'bcabaabaaacaccbbaabacaacbcc',
            'aacaabacaccacaaaaaaacaabacc',
            'ccaaacbaabcaacccbacaaaabaaa',
            'ccaaabbaaaaaabababbbbaacacc',
            'babbaaabcaabbabaaacabbaaaac',
            'acacacaacacccbbacacbccccacc',
            'aacbcbcccbbbcbaaaaaaaaabaaa',
            'baaaaacaaaacbbaacabccaaaabb',
            'ababcbbabaaaabaacabbaabcabb',
            'aababaaabbacaabcaacbaccbacb',
            'caababaaaababaaaabbabbbaaab',
            'aaaaaaaccbbbbacaccaccaabacb',
            'bacbcbaabaaaaacccacbaccaaac',
            'bbacaabaacabbcababacbbcaaca',
            'aaaacaaaaaacabababaaccccbac',
            'cacccaabacbcbabbcabbaccaaab',
            'abacababbccaaaabbcbaaaaaaaa',
            'aaacaaacaabaaaacbbbaaabbabc',
            'cacaacbbaccacccabcaacacabba']
        )
        expected = 868
        self.assertEqual(actual, expected)

    def testInput006(self):
        actual = strokesRequired(
            ['ccaccaacaacaaacccaaaacaaccaacacacacaccaaaaacacacabcacacacaaaaccaccaaaaaaaaacccbaccaccaacaaaacaacacaacccaaacaaaccaccaaaaacbaccacacaacacccaccccacabaaacaccccaaacacccccaaaaacaaccccccaaaaaaacaaccccaacacacaacacccacabaaccbaaacaacccaaccacccbaacccaccaaaaccacaaaaaccccaaaacccccccaaaaccaaaaaccaa',
            'abaacaaacacaaaaaaaaabaaacaacbcaccacccacaacbcaaacaaaacaaacacaaaacaaaaabccaaacaaacaaacacaacaacccccacccaaccaaccaacaaaccaaaaacacaacaaacaaaaaaaaaacaccacaaccacaacaccacaaaacacaaccccaacacacacaacccacaaaaacaaacacccaaaacacacaaacaacaacaaacaaacaaaaacaaacccaaaccaacacaaccccaacacaacacaaaaaaacaaacaca',
            'caccaaacacaccacccaaacccaacacaacacaaaabcaaacacacacaaaccaacaaaaaacabbacacaaacaacaaaccacaaccccaaccaaaacacaacccaacaaabacaaaccaaaccaaacaacccacabaaaaccacaaacaaaacccacacbaaccccaccaaaacacaacacacacacaaaccacccaaacaaccaaaaaccaacccacaaaaaccaccaaccaaccaccaaaaaaabcaaaacaacaccccaccaaaacacccacaccaaa',
            'cccacaacaaccacaaccaaccacbaaaccaaaacaaccaaaaccacacaacacacccaaaaaacaaaacabaaacaaaaacacccacaccacaaacaaccaaaaccccacaacaccaaaacaacaacacccacacaaaaaacaaaccaacaccaaccaabaccacaacaaacaacabcacaccaaacacacaaccaaaaacacaaccccacaaaacacbaccaacaaaaaccaaaccaacaabcacacacccaccaaaacaccaacaacacacccbbaaaaaa',
            'ccaaaaaaaaaccacacacaacaaaaaacaaccaacaaaaaaccaaccaacaaaccacaccccaacaccaaccaacacacccaacaaaacacaaaaacaaccaaaccaaaaacccacaaaaacccaaaccccacacaaacaccaccacaacaaaaaabccacaaaaaaacacaaaaccaaaaaaccacaaacaaacaaccaaacccacacaacbaaaacaaaaccccaccaacacaaacaccaaaccccaaacaaaaaaacacacaacaacaabcccbacccca',
            'aabbaaaacccacacaaccacccccccccaacaacaacaacaaacaacacacaaaaacccccaaacacccccccacccacaacaaaaaacacacaaaaacacaacacaacaaaacaaccaccaacccacccaccaacaacacaacaccaaaaacaaccaaacccacaaccacbaacacaacaaabaaccaccaaaaccaaccaaaccbacacaacaccaaccbcaacacaaacaaaacacacaaacaccacbaacaaaaaacacaaaaaacacaaacacbccac',
            'caaaaaccaccaaacaaaccaaaacccacaaccaaaacaaaaaacaaacaacaacaaaaacacaacacaaaccccaaaccacbcaaaaccabaaacaaccccccccccccaaaaaaacacacaaacacaaaacaacaccaaacacbaaaccaaacacccaacaaaacaaacaaccccaaacaabcaacbaccaaaaccacaaccacaccccaaaaaaacaacaaaaaaacaaaaaaaaaabacaaaacabaaaccaaaaacccaacaacccacaaacaaaacca',
            'caccacaaaaaaccaaaacaaccaccaccaccacacccaaaaaaccacaaccaacccaacccaaacaaaaaacaaaccaaaaacaacaaaabaaaabcaacaaaaabacaacccabaaacaaccaacaaaababacaaaaaaaaacaaaccccaaacacacaacacaacaaaaaaacaacacccaacaccaaacaacccaaccaccacaccacbaaaaaaccacccaaacaaaacaacaacaaacaccaaaaaaccaacbcaccaabaacaaaacacacbacac',
            'cccaaaacaacaaacccacacccacaaaaacaaaaaacccaabcaaaccaccbacacccaccaacccacaaaaaccccacacaacacaaccaaccaacaccaacccabaaaccaaaacaaaaaaaaaaaaacaccaacaaaaaaaaaaaacccacaacaccaacaaacbaaaaacaaaaaaaacccacacbaaaaaaaaaaabacaaccaacccacacaaaccacaacccacaaacacaaacaaacaacacabcacaaacaaaaaacaaaccabacccaccccc',
            'ccbccccacaacccaacaaccaaacacaaaaaaaaaaccaaaaaccacaaacaaccaacaaaccacaaaaabcaaaaaccccacacaacacaaaaccacbcacaaaaaccccaaacaaccabaaccaaaaccaacacacaacaaaacaaaccaaccacaaaccccacacaaacaaacaaaccacaccacaccaacaccccaaaacacaacccaaaacacacacacacacccacaccbaacaacaaaacaaccccacacaccccacaaccaaaaaaccccaacca',
            'caaaaaaaaaacaaaaaaaccaacaaaacaaacaccaaacacacaaccccacaacaaaaacacccaaaacccaaaaccaccaaaaccacaccccaacccaacccaaaaaaacccccaaccbaacacacaabacccaaaccaccaaaaaaacaaccacaaccaccaccaccacaaaacaccacaacaacaaaccbaaacacaaccaacaacaaaaccaaaacaaaccaaacaacacaaccbaaaaccaacacaaccacccacaaaaaaaacaccaaccaccaaaa',
            'bcaacabaacaacaacaaacaacccccacaaacacccccaaacccaabaaccaccacaacacccaaaaaaaccaaacaaacacacaaaacacaacaaccacaccaaaacaccacacaaacaacaaaaaacccccacaaacccabaaacaaaaaacccaacaccabaaccaccacacaaaaaccacaacaaacccaacacbabaaccaacaacccacccaacaacaaacaacaaaacacaaccacacacaacaaaaaaaaaaaccaaaccaacaccccccaacca',
            'accacaccacaaaaacaaccacabacacaaccaacccacccccaabacccaacaaaaccbaaaaaacaaccaaaaacaacacacacbaaaaaacacacaacccacaaaaaaaaccccaaaccaacaaaccaaaccccaaaaacacaaaaaacaaaaccaaccccbacaaacacacaccacaaabaacaaacacaaacacaccaccacacacacaaaaaaccabccaacacaacacacaccaacaaccacccaaacaacccaaccacccaaaacacaacaacacc',
            'acaaaacbaabcacaaccaacacaaaaaaccacaccaacacacaacaacaabccaacaaacaaacaaaaaaaaaaacaaaaaacccaaaaaaaaaaaaccaaccacaaaacaacaaaaabcaacccaaaaaacaaaabacaccaacacccacaaaaaaaaaaaaaccaaaaaaaaacacccaacaccacaacccaaccaacccaaacccaaaaaaaccaacaaaacaaaacaaacaccaaaacaaccacccaccacaaacccabcaccacacaacccbaacaaa',
            'aaaaaccbacacaaaacaccaaaaacaccaaaccaaccacaccacacaacacccccaaabaaaccccccaaccaaccaaaacccccaaccacccaacccaaaacacacbcaaaaccaaaaaaaaaacacbacacbacccaaaacaaaaabcaacacaaaaabaaaacaaaaaaaaaaaaaacaaccaaacccacacacaacaccaaaacaacaacaccccaaaacaaacaaaccacacaccaaacbcacaaaccaccacaaaccabccaacccaaacaaaaaaa',
            'cacaacaaaaaaccabcaacaaacaacccaaaacaaaaaaaacacccaccccacaaccaaaacacaaaacaaaaaaacacaaccaaacacaacaaaaccacaaaacaaaaccaaaccaaaaaacacaacaaacaaacccaacaaccaccaccacacaacccccaaccccaaaccaccccacacaaaaaacccccbbaaabccaaacaaaccccaacacccacaaaaaacaacaaaaaaacaaaccaaacaaaaaaccccabcaacaabccacaaaacaaacaaa',
            'ccacccacaaccccccaaccaaacaaaaaaacaccaccacacaaccacccacaacaccaaaaacabcaaaacaaacaacaaaacacaaaaaaaacacaaacaaccaccccaacaacccacccacaaaaaabccaaaccccaacaacaacacbacaaacccccaaaaacccaacacaaacaacacaccaaaacaaacacaaaaccbaaaacabcbacccaaacacacacaacacaaaaaccaaaaccaaaaacaaaacccaaaacaaacccaaaaaccaaccacc',
            'acccabaaaaaaacaccacaccacaaacabaaacacccacaacaacacaaaacabacaccccacaaacaaaaccabaacbacaacbaacaacccacacaaaacaaacaaaaaaaaaccacacaaacaacaaaaacccaaccaacaccaaaaccaaccaaaccacaacaccaccacaaacccccacabacccaccacacccaacaacaccaacacaaaaaccaccccaaacaaaacccaaaabccaccacacaccacccacacccaccacaaccaaccaacacbc',
            'acaaacccaaaaacaaaacaacaaacacaaacacaacaaacaaabcccaaacaacaccacacaaaacacabaaaaaaaacacaaaaccacacccaccaacaabacacccacacacbacacacccaacaaaaaccacaaaaaccccaaaabaaaccaaaaaaaacccccccaaaaccacacacaaaccccacaaccacaaccaaaaaaaaaaaacaccacaaacaacaaccaacacaacacccacbcaccacacccccaacaaccaaccaccaaaaaaacaaaca',
            'caaaccccaccaaaaaaaacccacccabcccaaacaccacaaaacacccaaccacbccaccaccbaaaaaabaaacccaaaaaaaaaacaacaaaaaaaaaaaccabaacacaacccaaaccaccacaaaaacaaacccacaaaaaaccaccabacaaacaaaccacaaccacacaccaccaaccaccccabacacaaacacaacaaaccaccaaccacaccaaacccaaccaaaaaccccaaacacaaaacaacacaaacaaaaaaaaccaaaacacaccaaa',
            'aaaaccacaacaaaaacaccccbccaaccacabacaccccaaaccccccaacccacaabaaaacaaccacccccaaacacacacaaaaaaaacacccacaccacaaacaacccaacacaacbcabaaccacaacccccacccaacaaaaccacacaacacacbccccccaccccccccaaaaacacccacaacaaaaccaaaaacacaaaaacaaaacaccacacaaaacccaaaaaacabcacaacacaaaabaaaacacaacaacacaaccaaaaacaccaa',
            'caaacbabcacaccaaaaaaccaabaaaacbacaaacacacaacaaacaaaaccaacaccabcaaccaacaaccaaccacaacccaacbaaaaacccccaccccaccaaaabaaaaccbcaacccaccaaaaaaaaaacaaacaaaacaacccaaaacacaacacacaaaacaaaacbaccccaaacacacaaccaacaacacacacaaaaaaccacabcaacaccccacaaccaaacacacacaaaacaaaaaaaccaaacaaaaacaaaaccaacacaaaca',
            'caacacccacccabcbaacaaccaccaacaaacaacabaacaccccaaacccaaaaaaaaaccaaacacaacaaaacaacccccaccaaabaacacacaaaaaccccaaaaacaacaaccaaaaccaccbacacccacaccaaacccaaabaaaacccaacccaaaaccaccccacacacaccaaaaaaaacaacaccaaacccaaccabaacbacacaaacaacccccaccaccaaacaaaaccaabacccaacccaaaccccaacacacacacccaaaacca',
            'aaaacaccaaaaaaacabacaacaccacaaccaaaaaaaaaacbaaaaacaccaaacaaacaaacaccacccacacaacacccaaccccacccccbcaaaacaaaacaacacaaaacccaaaaaacacccaaacaaccccaccccacaaaacacaaccacaaaaaaaaacaaaaaacaaaaacaaaaccaacaaaccacaaaaaaaaaaacacaaaacaaaaaaccaacacaaaaaabaacaccaacaaaaacbacaaacaccaaaacaaaccacaaaaaccac',
            'caacaaacaaaaccccccacccaaacabccacccaacaacccaacccccaacaaacaacaaaccabaacccaacaaaaaccacacaaaacaaacccaaaccacbbcacaaaaccaaaccaacccaacaaccacabacaaacaaccaaacccccccaacaacaaacacacaaaaaaacccabaaccccaaaacaaaaccaaaccacacaccacaaacaccacacacaccaacccacaaacacaacaacaaacaaaaaaaaacacaacaaaacaacaacaaccacc',
            'ccacccccacaccccacaccaaacccaaaaacaccaacacaaaaacaacaacaaaaaacacaaccaacaccccaaaaacccaaaaaacccaaabccacaaaaacacacccaaaaccaacacaaaaacaacacaaacaccccaaacccaaccacacaacaacaaccacaaaaaaccccacacaacaaaacacccaccaaaaaaaaccaaaacaaaaabaacacccbaaaacccccacabccccaaaacacaccacacacbaacaaaaaaacaccaccacaacccc',
            'cacaaaccaaaaccccaaaaacacaccaaaaccaaccaacacccaacccacaaacccccaaaaaaccacacaaaacaacaacaaaacacaaccccaaacaacacccaacccaaaaaaccaaaaacacaaccaaacacccccaaaacaaaaacacacaacacabacacaaacccccbcaacaaccacaaaccacacacaaabaacacacaaacbacaaaaaacaaccaaaaabbcaaaccacaaaaaacacaccacaaaaaacacaaaaaaacccacacaacacc',
            'aaaaaaccccaccacbaaaaccbaaaccaaaccccaccacacccacacaacbacaabaccacccacabcaacaacccaaaaacaaccccaacaaacaaaaaaacacabcacaaabaaaaacccaaaaaccacaaaaaabacbaccaabcacacacaacccacaaccaccacabaccabcacabccccaaaacaaacabacaaaaccccaacccccacaacacaacacacaacacaaccccaaccccaacccaacaaacaaaaacacbacccccacaaacacaca',
            'aaabaacaacacacaacaaaabaaaabacacccacccccaaaaccccaaaaccaccaaacaaaacccaaaaabacaaaccacaaaaacaabcacaacccaaaaccaccacccaacacccccccaaaaaaaaaccaaaacaaaaccccaacaacaaaccccccaaaacaacccaaaccacaaacaaaccccaaacaabaaaaacaaccacaaaaccaacaacaaaccaaccabacaacccaaaaaccacacacaacccaaaaaaaacaccaacaaaaacacacac',]
        )
        expected = 1460
        self.assertEqual(actual, expected)

    def testInput007(self):
        actual = strokesRequired(
            ['bacababbcacacbbbbcaccbcbcabacccaccccbcbbaaababcbcbaacbcb',
            'ccbcccbcbcbbbcbccbabbcabccccbbbcaabcbbccccccccbbbbbbbcbc',
            'abbacbacbbcaabcabbabaccccacbbbccbacbbcbccbcacccacacbbcbb',
            'cbcbacabbbbaabbcccbbccccabccbbbbabbabcccbcbacacbcbbbacab',
            'acabccbcccbabccabbabcabbbcbbbbcbabaccbcaabbcacbccbcbacba',
            'baccbcccabcbbbaaabcacabbbcaccaaccbcacacbcabbabccbcbacabb',
            'abccbbbaccccbaccabbbcccbcbbbbabaaccbcababccbbccbaabaacbb',
            'abcbccbabcbbacbccababcbcbcabcbbabbaacbbaabbccbbbacbaacba',
            'ccbbbccbbcabcbbcbbcbbbabcbcccbabbacbaccbbbacaaccababbbab',
            'bcbbacaacbaababbabbbaaacbbcbaaacbaacbbcbbbbcbcbaabccabba',
            'bbbacbcbbbaccbcbcacccbbabcbcbbccbcbcbbbbbabbbbaacbbccbbc',
            'abacabaccabbabcbbcbcaabbcbcbcabaabacbaabacbbcccbbbccaaaa',
            'ccbbbbbcbcbaacbcbbbabbbcbbcccbbabcbbabababaaccaabbbaaacb',
            'aabbacccbbbcccccaccbbbbacbbcabaacccbcaccaacabcaccbbccbab',
            'bcbbbbbbccbccbbbaaccacccbcbaababbbcaaccccbcaccabcbbcccab',
            'cabaccbcbaacbccacacacbcbbbbbabbbbccbcbabcbaabacabacbbbbb',
            'ccbbbbcababbbacbacbaabbbbcacbbcacacbcabacbbbabbbbcbbbbac',
            'aabaacabcbbaababbcbbcbbbcccccabbbbbacababbabbbcbbbbccaac',
            'abcaababccacbbabaccaacaccacbbbbcbbbbaccbccabbaabaaaacbbb',
            'babccbbabbbbbacccbbcbbccbbbbbbcccbbcccbaccbcbcccbacccbab',
            'cccbacaaccaaccbbcbbbbcbbabcccbbabccbabcaababccbbcbbabcca',
            'bbabccacabababbbbcbcaabbcbbcbbcbbabbbaacacbbacabaccbaccc',
            'caabbcbbbbcbbcbbbbbbcbbacccbacbaacabacbccbbbbcccabbbcccb',
            'bbcbbcaacccabbcabccbbcaccccccbcabbbccabcabbbbabcbcabbbcc',
            'abacbbbbccccabbbbcccbccacbcbabbccabccbbbccaccbbbcbbbcbcb',
            'abcccacbcabbcbbbacacbcccccabccabaacbcbbbaabbbabbaabbabbc',
            'bbcbcbbcbbbbbabcbcbabaababbccbabccabbbaabbaccabccccbbaab',
            'bcbbbbcbbbbbabbbcbcbccbbbcbbbbcccccccbbbaabcbbcbccbaccbb',
            'acccbbbaaacccabbcbcbcccccbcbbacccbcbbaabcbbbcbcacbbbcbbb',
            'caabcccccbbcccbcacaabcbccaabbcacbbababbcbcbbbcbbccbbcccc',
            'bccbbbacacbcacabcbccccbbabbbcababcabbbbccbaaccaccbbcbaab',
            'ababaaaabaabbaccaacccbbbbabbaacbcbcbbbbccbbbcccabbaaacbb',
            'cccccccacacacabbbbcbabcabbabacbbccccbacbbbbbbbcabbbbbccb',
            'abababbcbbbcccbcacbcbacababbcbabaccccabbbbbcccccbccbcbbc',
            'bcbbbbbcbbccccbbccccabaababbbaacaabbbcccbbbbbabaccbcbbba',
            'bbcaaccabbcbbacccbbbabcbbbbbabcacbccaacccbabcbccbccccbbc',
            'cbbbbaabcbcbcaabbccbccbbbcbcbacccbcbbbcabbccaabbcacbaaac',
            'ccaacbbbbbbbbbaaccccbbccbaaaaccbbaacccaccbbcaaaacabcbbba',
            'babbabccbacaabbcbabccbbbaccbccabbbbbaccaabcbcabcccccbcab',
            'bbbacacabbbbbcaccabccbccccbbbccbccbacbabccababbbbbabcaaa',
            'cbbcacccbabbaabcabbbbcbcaacaccabcbcacbbacacbbbcbcbcbcccc',
            'abcaacbcbbabccaccaacbbabbacbbbbbcbacbbbacccccbbcaabacabb',
            'bcbacbabccccccccbcbabaabacbbbbbbccbccbaaccbccbbbccabcacc',
            'abaacaabbcccbbacbbbabacbcbacabacabcbbababacabbccbacaacbc',
            'cccbbcccbcccbacbabbbabbcbacbbbcbcbcbcccabacaaabccabbbacb',
            'bbbbccabbacacbaaccabbbbbbcbcbbcbcacbacbcabcaacbbbcaccbba',
            'bcaacbbbbababbbcabbccaccbacbcbbabbccbcabbbcabbbcaccccbab',
            'bbccbbcbccbacbabbccbabbccaabbbcbccbcccbbccbcccbccbccbbac',
            'bbcbabbacbccbcbcbaabcbabababcaababcccacccbaaccbbbbababaa',
            'bbcbabbccbcabbbccabbacbbbbcbbacbcbbbacbbcbbbcacabcbcabab',
            'bbbcbacabbccabbacbbbbacbbababbacacbcababbcbbbccbcccbcaab',
            'acbbbcccabbbcbbbbbbbbbbacbbacbbcbabcaccbbacbaacaabbccbac',
            'ccbaabbabbcbbcbbacacbaaccbbacbbbcaccbbccccbccccacbcbbccc',
            'baabcbbbbbbcbbcacabbcaabaacbcbbcbacacbabbcccbcbcbcababcb',
            'cbccccabcbbbabcbbababbaacbcbbcbabcbccbcacccccbbbbcccbccc',
            'ccbbabacbbbabcbcbcccccbcbcbcbccbaaccaccbcabaccbabbbbcbba',
            'cbbcbcbbbccbacaccbbcaacbbcacacccbbbbacabbcaabcccababbabc',
            'cbcbbabcbbbbcbbbbbbcaaacbaccacbbbbaabcaacbcbcbcababcbbcb',
            'abacabbccccbcccbcccbbabbcacabaabaabbbcbcbcbbcbabcbbababb',
            'bbbcabbcbbcbcbbcbcbcabbbbccbbaaabccabbccaccbbccbbbbcccbb',
            'ccbbbcaccbacbbcbbccbaaabbbbcccbbccbababaaaaccbcbbcbaabbb',
            'cacbccaacaabbbbaaaabcbbabbbcbccbbacbcbbacacbccbcbabbacca',
            'bccbbabcabcbcabacaabcbbbbaacccccabbcbbacbabbcccbcbcbabbc',
            'cbbbaacccbcbbcbbaacabcbbbcacbbcaaacbbbcbcbbbbaababbaabca',
            'bacbcacabcbcbabcaccaabacccbbccacabcaaabbacccbccbcccbbbac',
            'acccbcbbbacbbbbaacbbbbcacbbbaabbccbbcabbcbcbbbabbbaacbbb',
            'bbbbcaaaaabbbcbabbababbabcabccabbbbbbacbbccccbcbcbbccacb',
            'bbbbaaccbbacacbbbcacccabbccacbbbbcbaaaaacbcbbbbcbbbaccab',
            'ababbbbccbbbabaccaaabbbabcbbccaaccbccbbaabaabbccccccbccb',
            'accbbbbbcccccbbcccbbccbbbbbaaababcbbcbccbbcabbaccacbcccc',
            'cbcbabcacbbcbcbbbcbacbcacbaabcbbbcbbbacbacbbcbbbaaaaabbb',
            'babccccaccaaccbbaccccacabcbcbccccacbbcbccbbccbcccbcbcbcc',
            'cabbbbcabcbabcbabcccbcaccbbcbbbcbbaabcaabccabacaaabacbcb']
        )
        expected = 1406
        self.assertEqual(actual, expected)