using System;
using System.Windows.Forms;
using MarketTracker.UI;

namespace MarketTracker
{
    static class Program
    {
        [STAThread]
        static void Main()
        {
            ApplicationConfiguration.Initialize(); // .NET 6+/WinForms template
            Application.Run(new MainForm());
        }
    }
}
