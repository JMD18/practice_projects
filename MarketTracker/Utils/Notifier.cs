using System.Windows.Forms;

namespace MarketTracker.Utils
{
    public static class Notifier
    {
        public static void Notify(string message)
        {
            MessageBox.Show(message, "Market Alert", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }
    }
}
