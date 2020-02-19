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
        return self.get_all_counties()[county_name.lower()]

    def get_precinct(self, precinct_name):
        """
        :return: A dictionary of how many votes each candidate has in the precinct
        {"sanders": 100, "biden":20, ..., "reported": True, etc}
        """
        return self.get_all_precincts()[precinct_name.lower()]


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
        votes = {'Klobuchar': 0, 'Sanders': 0, 'Warren': 0, 'Yang': 0, 'Steyer': 0, 'Biden': 0, 'Buttigieg': 0}
        for candidate in data['data']['races'][0]['candidates']:
            try:
                votes[candidate['last_name']] += candidate['votes']
            except KeyError:
                pass
        votes['precinct_total'] = data['data']['races'][0]['precincts_reporting']
        votes['precinct_counted'] = data['data']['races'][0]['precincts_total']
        return votes

    def get_all_counties(self):
        county_results = {}
        data = self.get_data()
        county_raw = data['data']['races'][0]['counties']
        for place in county_raw:
            votes = {'Klobuchar': 0, 'Sanders': 0, 'Warren': 0, 'Yang': 0, 'Steyer': 0, 'Biden': 0, 'Buttigieg': 0}
            for name, num in place['results'].items():
                for key in votes.keys():
                    if key.lower() in name:
                        votes[key] = num
            county_results[place['name'].lower()] = votes
        return county_results

    def get_all_precincts(self):
        precinct_results = {}
        data = self.get_data()
        town_results = data['data']['races'][0]['townships']
        for place in town_results:
            votes = {'Klobuchar': 0, 'Sanders': 0, 'Warren': 0, 'Yang': 0, 'Steyer': 0, 'Biden': 0, 'Buttigieg': 0}
            for name, num in place['results'].items():
                for key in votes.keys():
                    if key.lower() in name:
                        votes[key] = num
            precinct_results[place['name'].lower()] = votes
        return precinct_results

    def get_county(self, county_name):
        """
        :return: A dictionary of how many votes each candidate has in the county
        {"sanders": 100, "biden":20, ..., "precinct_total": 50, "precinct_counted": 12, etc}
        """
        return self.get_all_counties()[county_name.lower()]

    def get_precinct(self, precinct_name):
        """
        :return: A dictionary of how many votes each candidate has in the precinct
        {"sanders": 100, "biden":20, ..., "reported": True, etc}
        """
        return self.get_all_precincts()[precinct_name.lower()]
        
    def DDHQResultsVotes():
        """
        :return: A dictionary of how many votes each candidate has from DDHQ's API, 
        {"sanders":100, "biden":20, ..., total: 200}
        currently set to NH URL API
        """
        data = requests.get("https://results.decisiondeskhq.com/api/v1/results/?limit=1&election=1ee05d83-2d5b-48ad-8c07-dfd6f63344be&electionType=primary").json()
        
        for races in 
        results = data['results'][0]['votes']
        try:
            votes = {'Klobuchar': results['8233'], 'Sanders': results['8'], 'Warren': results['8284'], 'Yang': results['11920'], 'Steyer': results['11921'], 'Biden': results['11918'], 'Buttigieg': results['11919'], 'Total':0 }
        except KeyError:
            pass
        for candidate in results:
            votes['Total'] += results[candidate]
        
            



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


nyt = AP("https://int.nyt.com/applications/elections/2020/data/api/2020-02-11/new-hampshire/president/democrat.json")
print(nyt.get_all_precincts())
print(nyt.get_precinct('acworth'))
print(nyt.get_totals())