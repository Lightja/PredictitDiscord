import requests


class DDHQ:
    def __init__(self, url):
        self.url = url

    def get_data(self):
        """
        Uses API to get json vote data
        :return: A dictionary of the raw vote data from AP
        """
        return requests.get(url=self.url).json()

    def get_totals(self):
        """
        :return: A dictionary of how many votes each candidate has in the state
        {"sanders": 1234, "biden":1200, ..., "precinct_total": 400, "precinct_counted": 132, etc}
        """
        data = self.get_data()
        return {}  # TODO

    def get_all_counties(self):
        data = self.get_data()
        return {}  # TODO

    def get_all_precincts(self):
        data = self.get_data()
        return {}  # TODO

    def get_county(self, county_name):
        """
        :return: A dictionary of how many votes each candidate has in the county
        {"sanders": 100, "biden":20, ..., "precinct_total": 50, "precinct_counted": 12, etc}
        """
        return self.get_all_counties()[county_name]

    def get_precinct(self, precinct_name):
        """
        :return: A dictionary of how many votes each candidate has in the precinct
        {"sanders": 100, "biden":20, ..., "reported": True, etc}
        """
        return self.get_all_precincts()[precinct_name]


class AP:
    def __init__(self, url):
        self.url = url

    def get_data(self):
        """
        Uses API to get json vote data
        :return: A dictionary of the raw vote data from AP
        """
        return requests.get(url=self.url).json()

    def get_totals(self):
        """
        :return: A dictionary of how many votes each candidate has in the state
        {"sanders": 1234, "biden":1200, ..., "precinct_total": 400, "precinct_counted": 132, etc}
        """
        data = self.get_data()
        return {}  # TODO

    def get_all_counties(self):
        data = self.get_data()
        return {}  # TODO

    def get_all_precincts(self):
        data = self.get_data()
        return {}  # TODO

    def get_county(self, county_name):
        """
        :return: A dictionary of how many votes each candidate has in the county
        {"sanders": 100, "biden":20, ..., "precinct_total": 50, "precinct_counted": 12, etc}
        """
        return self.get_all_counties()[county_name]

    def get_precinct(self, precinct_name):
        """
        :return: A dictionary of how many votes each candidate has in the precinct
        {"sanders": 100, "biden":20, ..., "reported": True, etc}
        """
        return self.get_all_precincts()[precinct_name]


class Model:
    def __init__(self, precinct_historical, precinct_current):
        self.precinct_historical = precinct_historical
        self.precinct_current = precinct_current

    def update_count(self, precinct_current):
        self.precinct_current = precinct_current

    def extrapolate(self):
        for precinct_name, vote_dict in self.precinct_current.items():
            try:
                prev_total = self.precinct_historical[precinct_name]
                for candidate, vote_total in vote_dict:
                    pass  # TODO
            except KeyError:
                pass  # TODO
