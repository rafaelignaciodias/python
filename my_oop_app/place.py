class Place:
    place_list = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._status = False

        Place.place_list.append(self)

    def __str__(self):
        return f"{self.name} | {self.category} | {self.status}"

    def list_places():
        for place in Place.place_list:
            print(place)

    @property
    def status(self):
        return "Active" if self._status else "Inactive"


new_place = Place("new place", "super category")
new_place = Place("old place", "fast  category")

Place.list_places()
