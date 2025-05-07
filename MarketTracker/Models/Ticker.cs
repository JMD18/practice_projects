namespace MarketTracker.Models
{
    public class Ticker
    {
        public string Symbol { get; set; }
        public decimal? LatestPrice { get; set; }
        public DateTime LastUpdated { get; set; }
    }
}
