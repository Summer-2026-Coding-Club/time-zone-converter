from datetime import datetime
import pytz
from colorama import Fore, Style, init

init(autoreset=True)

# Cities with their time zones and flag emojis
cities = {
    "New York": {"tz": "America/New_York", "flag": "🇺🇸", "region": "North America"},
    "Denver": {"tz": "America/Denver", "flag": "🇺🇸", "region": "North America"},
    "Little Rock": {"tz": "America/Chicago", "flag": "🇺🇸", "region": "North America"},
    "London": {"tz": "Europe/London", "flag": "🇬🇧", "region": "Europe"},
    "Rome": {"tz": "Europe/Rome", "flag": "🇮🇹", "region": "Europe"},
    "Istanbul": {"tz": "Europe/Istanbul", "flag": "🇹🇷", "region": "Europe/Asia"},
    "Dubai": {"tz": "Asia/Dubai", "flag": "🇦🇪", "region": "Middle East"},
    "Gaza": {"tz": "Asia/Gaza", "flag": "🇵🇸", "region": "Middle East"},
    "Karachi": {"tz": "Asia/Karachi", "flag": "🇵🇰", "region": "South Asia"},
    "Jakarta": {"tz": "Asia/Jakarta", "flag": "🇮🇩", "region": "Southeast Asia"},
    "Kuala Lumpur": {"tz": "Asia/Kuala_Lumpur", "flag": "🇲🇾", "region": "Southeast Asia"},
    "Cairo": {"tz": "Africa/Cairo", "flag": "🇪🇬", "region": "Africa"},
    "Lagos": {"tz": "Africa/Lagos", "flag": "🇳🇬", "region": "Africa"},
    "Tokyo": {"tz": "Asia/Tokyo", "flag": "🇯🇵", "region": "East Asia"},
    "Sydney": {"tz": "Australia/Sydney", "flag": "🇦🇺", "region": "Oceania"},
    "Toronto": {"tz": "America/Toronto", "flag": "🇨🇦", "region": "North America"},
}

# Group cities by region for a "map-like" display
regions = {}
for city, info in cities.items():
    regions.setdefault(info["region"], []).append(city)


def play_chime():
    """A little text-based 'sound effect' for fun."""
    print(Fore.MAGENTA + "♪ ding! ♪" + Style.RESET_ALL)


def show_world_map():
    print(Fore.CYAN + Style.BRIGHT + "\n🌍 ===== WORLD TIME MAP ===== 🌍\n" + Style.RESET_ALL)
    for region, region_cities in regions.items():
        print(Fore.YELLOW + Style.BRIGHT + f"\n📍 {region}" + Style.RESET_ALL)
        for city in region_cities:
            flag = cities[city]["flag"]
            print(Fore.WHITE + f"   {flag}  {city}" + Style.RESET_ALL)


def show_time(city):
    info = cities[city]
    tz = pytz.timezone(info["tz"])
    current_time = datetime.now(tz)

    print(Fore.GREEN + f"\n{info['flag']}  {city} ({info['region']})" + Style.RESET_ALL)
    print(Fore.WHITE + Style.BRIGHT + current_time.strftime("🕐 %A, %B %d, %Y - %I:%M %p") + Style.RESET_ALL)

    hour = current_time.hour
    if 5 <= hour < 12:
        print(Fore.YELLOW + "☀️  Good morning there!" + Style.RESET_ALL)
    elif 12 <= hour < 17:
        print(Fore.YELLOW + "🌤️  Good afternoon there!" + Style.RESET_ALL)
    elif 17 <= hour < 21:
        print(Fore.MAGENTA + "🌆  Good evening there!" + Style.RESET_ALL)
    else:
        print(Fore.BLUE + "🌙  It's nighttime there!" + Style.RESET_ALL)

    play_chime()


def main():
    print(Fore.CYAN + Style.BRIGHT + "=" * 40)
    print("🌍  WELCOME TO THE TIME ZONE CONVERTER  🌍")
    print("=" * 40 + Style.RESET_ALL)

    show_world_map()

    print(Fore.GREEN + "\nType a city name from the map above (or 'quit' to exit):" + Style.RESET_ALL)

    while True:
        city_input = input(Fore.GREEN + "\n> " + Style.RESET_ALL).strip()

        if city_input.lower() == "quit":
            print(Fore.CYAN + "\n👋 Goodbye! Thanks for exploring time zones with us!" + Style.RESET_ALL)
            break
        elif city_input in cities:
            show_time(city_input)
        else:
            print(Fore.RED + "Sorry, that city isn't on our map yet. Try another, or add it yourself!" + Style.RESET_ALL)


if __name__ == "__main__":
    main()
