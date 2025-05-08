def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    average = calc_average(num_list)
    min_max = find_min_max(num_list)
    sorted_list = sort_temperature(num_list)
    median = calc_median_temperature(num_list)

    print(f"\nResults:")
    print(f"Average Temperature: {average:.2f}")
    print(f"Minimum and Maximum Temperatures: {min_max}")
    print(f"Sorted Temperatures: {sorted_list}")
    print(f"Median Temperature: {median:.2f}")

def display_main_menu():
    print("Main Menu")
    print("1. Enter temperatures")
    print("2. Show results")
    print("3. Exit")

def get_user_input():
    print("Enter temperatures separated by commas (e.g. 22.5,24,19.8):")
    input_str = input()
    temp_list = [float(temp.strip()) for temp in input_str.split(",") if temp.strip()]
    return temp_list

def calc_average(temperatures):
    print("Calculating average...")
    return sum(temperatures) / len(temperatures)

def find_min_max(temperatures):
    print("Finding min and max...")
    return [min(temperatures), max(temperatures)]

def sort_temperature(temperatures):
    print("Sorting temperatures...")
    return sorted(temperatures)

def calc_median_temperature(temperatures):
    print("Calculating median...")
    sorted_temps = sorted(temperatures)
    n = len(sorted_temps)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_temps[mid - 1] + sorted_temps[mid]) / 2
    else:
        return sorted_temps[mid]

if __name__ == "__main__":
    main()
