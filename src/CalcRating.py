# -*- coding: utf-8 -*-
from Types import DataType, RatingType


class CalcRating:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}

    def calc(self) -> RatingType:
        self.rating = {}
        for key in self.data:
            scores = self.data[key]
            if not scores:
                self.rating[key] = 0.0
                continue
            total = sum(score for _, score in scores)
            self.rating[key] = total / len(scores)
        return self.rating
