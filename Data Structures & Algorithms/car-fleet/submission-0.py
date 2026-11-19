class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Сортировка обратная по позиции, что бы можно было сравнивать время со следующими 
        # Машинами
        cars = list(zip(position, speed))
        cars.sort(key=lambda car: car[0], reverse=True)
        fleets = 0
        last_fleet_time = 0
        for i in range(len(cars)):
            time_curr = ((target - cars[i][0]) / cars[i][1])
            if time_curr > last_fleet_time:
                fleets += 1
                last_fleet_time = time_curr
            else:
                continue

        return fleets
