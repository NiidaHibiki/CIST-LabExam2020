import MeCab


def print_words_and_results(raw_text: str = 'すもももももももものうち'):
    m = MeCab.Tagger()
    print(m.parse(raw_text))


def print_morpheme(raw_text: str = 'すもももももももものうち'):
    pass


if __name__ == '__main__':
    print_words_and_results()
