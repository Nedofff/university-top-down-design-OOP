


class Tourist:
    pass

class TravelAgency:
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