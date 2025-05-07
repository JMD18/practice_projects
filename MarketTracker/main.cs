using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using MarketTracker.Services;
using MarketTracker.Models;

namespace MarketTracker
{
    class Program
    {
        static async Task Main(string[] args)
        {
            var fetcher = new PriceFetcher();
            var watchlist = new List<Ticker>();

            Console.WriteLine("== Market Tracker ==");
            Console.WriteLine("Commands: add [symbol], remove [symbol], list, fetch, quit");

            while (true)
            {
                Console.Write("> ");
                var input = Console.ReadLine()?.Trim();
                if (string.IsNullOrWhiteSpace(input)) continue;

                var parts = input.Split(' ', 2, StringSplitOptions.RemoveEmptyEntries);
                var command = parts[0].ToLower();
                var argument = parts.Length > 1 ? parts[1].ToUpper() : "";

                switch (command)
                {
                    case "add":
                        if (!string.IsNullOrWhiteSpace(argument) &&
                            !watchlist.Exists(t => t.Symbol == argument))
                        {
                            watchlist.Add(new Ticker { Symbol = argument });
                            Console.WriteLine($"Added {argument}.");
                        }
                        break;

                    case "remove":
                        watchlist.RemoveAll(t => t.Symbol == argument);
                        Console.WriteLine($"Removed {argument}.");
                        break;

                    case "list":
                        if (watchlist.Count == 0)
                        {
                            Console.WriteLine("Watchlist is empty.");
                        }
                        else
                        {
                            Console.WriteLine("Watchlist:");
                            foreach (var t in watchlist)
                                Console.WriteLine($"- {t.Symbol}");
                        }
                        break;

                    case "fetch":
                        if (watchlist.Count == 0)
                        {
                            Console.WriteLine("Watchlist is empty.");
                        }
                        else
                        {
                            Console.WriteLine("Fetching prices...");
                            foreach (var t in watchlist)
                            {
                                var price = await fetcher.GetLatestPrice(t.Symbol);
                                if (price.HasValue)
                                {
                                    t.LatestPrice = price;
                                    t.LastUpdated = DateTime.Now;
                                    Console.WriteLine($"{t.Symbol}: ${price.Value:F2} @ {t.LastUpdated:T}");
                                }
                                else
                                {
                                    Console.WriteLine($"{t.Symbol}: Failed to fetch.");
                                }
                            }
                        }
                        break;

                    case "quit":
                        Console.WriteLine("Goodbye!");
                        return;

                    default:
                        Console.WriteLine("Unknown command.");
                        break;
                }
            }
        }
    }
}
