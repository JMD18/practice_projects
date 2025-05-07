private async void btnCheckPrice_Click(object sender, EventArgs e)
{
    var service = new FinnhubService();
    string ticker = txtTicker.Text.ToUpper();

    var price = await service.GetLatestPrice(ticker);
    if (price.HasValue)
    {
        lblPriceResult.Text = $"{ticker}: ${price.Value}";
    }
    else
    {
        lblPriceResult.Text = $"Failed to fetch price for {ticker}.";
    }
}
