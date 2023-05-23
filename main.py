


class TravelAgency:
    __count_tips = 0
    __map_places = ["Istanbul", "Ankara", "Sochi", "Gelendzhik", "Denpasar", "Paris"]
    __degree_of_comfort = [1, 2, 3, 4, 5]

    def set_tips_count(self, count):
        pass

    def get_tip(self):
        pass

    def get_tips(self):
        pass


class Tourist:
    tips = []

    def set_variants(self, tips):
        pass

    def get_choice(self):
        pass

def main():
    travel_agency = TravelAgency()
    tourist = Tourist()

    travel_agency.set_tips_count(10)
    travel_agency_tips = travel_agency.get_tips()

    tourist.set_variants(travel_agency_tips)

    print(tourist.get_choice())



if __name__ == '__main__':
    main()