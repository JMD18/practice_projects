using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;

namespace MarketTracker.Services
{
    public class PriceFetcher
    {
        private static readonly HttpClient httpClient = new HttpClient();
        private const string ApiKey = "d0dc9o9r01qhd59vjgl0d0dc9o9r01qhd59vjglg";

        public async Task<decimal?> GetLatestPrice(string symbol)
        {
            var url = $"https://finnhub.io/api/v1/quote?symbol={symbol}&token={ApiKey}";

            try
            {
                var response = await httpClient.GetAsync(url);
                response.EnsureSuccessStatusCode();
                var json = await response.Content.ReadAsStringAsync();

                using var doc = JsonDocument.Parse(json);
                if (doc.RootElement.TryGetProperty("c", out var price))
                {
                    return price.GetDecimal();
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error fetching price: {ex.Message}");
            }

            return null;
        }
    }
}
