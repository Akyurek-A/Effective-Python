import math


class Rates:

    @staticmethod
    def interest_calculation():
        initial_capital = float(input("Enter the initial capital [in dollars]: "))
        interest_rate = float(input("Please enter the interest rate [in %]: ")) / 100
        years = int(input("Enter the investment period [in years]: "))

        capital = initial_capital
        for year in range(1, years + 1):
            capital += capital * interest_rate
            print(f"Capital after {year} year(s): {capital}")


    @staticmethod
    def average_calculation():
        n = int(input("How many numbers should be analyzed: "))
        numbers = [0] * n

        for i in range(n):
            numbers[i] = float(input("Next number: "))

        print("OK. The numbers are:", end=" ")
        for num in numbers:
            print(f"{num}", end=" ")

        min_num = min(numbers)
        max_num = max(numbers)
        avg = sum(numbers) / len(numbers)

        print()
        print(f"Min: {min_num}, Max: {max_num}, Average: {avg}")

    @staticmethod
    def mult(vec, factor):
        return [v * factor for v in vec]

    @staticmethod
    def plus(vec1, vec2):
        return [v1 + v2 for v1, v2 in zip(vec1, vec2)]

    @staticmethod
    def minus(vec1, vec2):
        return [v1 - v2 for v1, v2 in zip(vec1, vec2)]

    @staticmethod
    def rotate2d(vec, deg):
        rad = math.radians(deg)
        cos_angle = math.cos(rad)
        sin_angle = math.sin(rad)

        x = cos_angle * vec[0] - sin_angle * vec[1]
        y = sin_angle * vec[0] + cos_angle * vec[1]

        return [x, y]

    @staticmethod
    def vlength(vec):
        return math.sqrt(sum(v ** 2 for v in vec))

    @staticmethod
    def vector_test():
        v1_x = float(input("Vector 1, x: "))
        v1_y = float(input("Vector 1, y: "))
        v2_x = float(input("Vector 2, x: "))
        v2_y = float(input("Vector 2, y: "))
        factor = float(input("Factor: "))
        angle = int(input("Angle (in degrees): "))

        vec1 = [v1_x, v1_y]
        vec2 = [v2_x, v2_y]

        v1_mult_fact = Rates.mult(vec1, factor)
        v1_plus_v2 = Rates.plus(vec1, vec2)
        v1_minus_v2 = Rates.minus(vec1, vec2)
        vlength_v1 = Rates.vlength(vec1)
        rotated_v1 = Rates.rotate2d(vec1, angle)

        print(f"v1 * fact : ( {v1_mult_fact[0]:.1f} {v1_mult_fact[1]:.1f} )")
        print(f"v1 + v2 : ( {v1_plus_v2[0]:.1f} {v1_plus_v2[1]:.1f} )")
        print(f"v1 - v2 : ( {v1_minus_v2[0]:.1f} {v1_minus_v2[1]:.1f} )")
        print(f"vlength (v1) : {vlength_v1:.1f}")
        print(f"rotate(v1, deg) : ( {rotated_v1[0]:.1f} {rotated_v1[1]:.1f} )")

    @staticmethod
    def main():
        while True:
            print("\n1 : Interest calculation")
            print("2 : Average calculation")
            print("3 : Vector test")
            print("0 : Exit\n")
            choice = int(input("Your choice: "))

            if choice == 1:
                Rates.interest_calculation()
            elif choice == 2:
                Rates.average_calculation()
            elif choice == 3:
                Rates.vector_test()
            elif choice == 0:
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")

Rates.main()
