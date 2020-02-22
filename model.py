from votes import AP, DDHQ, MergeResults


class Model:
    def __init__(self, state, date, alignment):
        self.ap = AP(state, date, alignment)
        self.ddhq = DDHQ(state)

    def merge(self):
        return MergeResults(self.ap.get_all_counties(), self.ddhq.get_all_counties())

    def merged_totals(self):
        return self.merge()['Total']

    def best_county(self, county):
        return self.merge()[county]
