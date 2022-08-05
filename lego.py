import asyncio

import aiohttp
from fpl import FPL


async def main():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        user = await fpl.get_user(511906)
        picks = await user.get_picks()
        players = await fpl.get_players(include_summary=True)

        print(f"{user}\n---")
        total_captain_points = 0

        for gameweek, gw_information in picks.items():
            captain = next(player for player in gw_information["picks"]
                        if player["is_captain"])
            player = next(player for player in players
                        if player.id == captain["element"])
            points = player.history[gameweek - 1]["total_points"] * 2

            total_captain_points += points
            print(f"Gameweek {gameweek:>2}: captained {player.web_name:<10} "
                f"for {points:>2} points")

        print(f"---\nTotal captain points: {total_captain_points}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())