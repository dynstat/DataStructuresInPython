# Example of graph using cities and roads as vertices and edges respectively.
class City:  # Vertex
    def __init__(self, city_name):
        self.name = city_name
        self.roads = []

    def __repr__(self):
        return self.name


class Road:  # Edge
    def __init__(self, road_name, city_from, city_to, r_length=None):
        self.road_name = road_name
        self.city_from = city_from
        self.city_to = city_to
        self.road_length = r_length

    def __repr__(self) -> str:
        return self.road_name


class Graph:
    def __init__(self, list_of_cites: list = [], list_of_roads: list = []):
        self.cities = list_of_cites
        self.roads = list_of_roads

    def add_city(self, new_city_name):
        new_city = City(new_city_name)
        self.cities.append(new_city)

    def add_road(self, new_road_name, city_from, city_to):
        from_found = None
        to_found = None

        # checking whether "city_from" and "city_to" already exist in our list of cities
        for city_obj in self.cities:
            if city_obj.name == city_from:
                from_found = city_obj
            if city_obj.name == city_to:
                to_found = city_obj
        if from_found is None:
            from_found = City(city_from)
            self.cities.append(from_found)
        if to_found is None:
            to_found = City(city_to)
            self.cities.append(to_found)

        new_road = Road(new_road_name, from_found, to_found)
        self.roads.append(new_road)


if __name__ == "__main__":
    cities = [City("Delhi"), City("Pune"), City("Mumbai")]
    roads = [Road("NH-8", "Delhi", "Pune"), Road("NH-24", "Delhi", "Mumbai")]

    g1 = Graph(cities, roads)
    print("INITIAL")
    print("All cities of g1 = ", g1.cities)
    print("All roads of g1 = ", g1.roads)

    g1.add_city("Himachal Pradesh")  # Adding a new city using add_city method
    g1.add_road("Yamuna-Express Way", "Noida", "Agra")
    print("UPDATED")
    print("All cities of g1 = ", g1.cities)
    print("All roads of g1 = ", g1.roads)
