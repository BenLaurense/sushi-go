from Cards.cards import *


"""
Methods for calculating score
Each method applies to a SINGLE CardType but is vectorised across players

Final method calculate_score vectorises these across CardType
"""


def score_nigiri(stats):
    return stats


def score_maki(stats):
    num_players = len(stats)

    sorted_scores = list(set(stats.copy()))
    if len(sorted_scores) < 2:
        return [6]*len(stats)
    elif num_players > 5 and len(sorted_scores) < 3:
        sorted_scores.append(-1)

    sorted_scores.sort()
    if num_players == 2:
        largest_scores = sorted_scores[-2:]
    else:
        largest_scores = sorted_scores[-3:]

    maki_score = [0]*num_players
    for i in range(num_players):
        if stats[i] == largest_scores[-1]:
            maki_score[i] = 6
        elif num_players > 5 and stats[i] == largest_scores[-2]:
            maki_score[i] = 4
        elif stats[i] == largest_scores[-2]:
            maki_score[i] = 3
        elif num_players > 5 and stats[i] == largest_scores[-3]:
            maki_score[i] = 2

    return maki_score


def score_temaki(stats):
    num_players = len(stats)
    max_count, min_count = max(stats), min(stats)

    temaki_score = [0]*num_players
    for i in range(num_players):
        if stats[i] == max_count:
            temaki_score[i] = 4
        elif stats[i] == min_count and num_players > 2:
            temaki_score[i] = -4

    return temaki_score


def score_dumpling(stats):
    def mapper(s):
        if s > 4:
            return 15
        return [0, 1, 3, 6, 10][s]
    return list(map(lambda s: mapper(s), stats))


def score_eel(stats):
    def mapper(s):
        if s > 1:
            return 7
        return [0, -1][s]
    return list(map(lambda s: mapper(s), stats))


def score_onigiri(stats):
    def mapper(s):
        digits = [int(d) for d in str(s)]
        digits += [0]*(5-len(digits))
        digits.sort()
        partials = [digits[i] - digits[i-1] for i in range(1, len(digits))]
        return sum([partials[i]*(4-i)**2 for i in range(len(partials))])

    return list(map(lambda s: mapper(s), stats))


def score_sashimi(stats):
    return list(map(lambda s: s//3, stats))


def score_tempura(stats):
    return list(map(lambda s: s//2, stats))


def score_tofu(stats):
    def mapper(s):
        if s > 2:
            return 0
        return [0, 0, 5][s]
    return list(map(lambda s: mapper(s), stats))


scorers = {
    CardType.nigiri: score_nigiri,
    CardType.maki: score_maki,
    CardType.dumpling: score_dumpling,
    CardType.eel: score_eel,
    CardType.onigiri: score_onigiri,
    CardType.sashimi: score_sashimi,
    CardType.tempura: score_tempura,
    CardType.tofu: score_tofu,
}


def calculate_score(card_types, num_players, stats):
    """
    Vectorises score calculation across CardTypes
    """
    scores_dictionary = {card_type: scorers[card_type](stats[card_type]) for card_type in card_types}

    scores = [0]*num_players
    for key in scores_dictionary:
        scores = list(map(lambda x, s: x + s, scores, scores_dictionary[key]))
    return scores
