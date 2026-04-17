using System.Windows;

namespace MultiplicationTable
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            LoadMultiplicationTable();
        }

        private void LoadMultiplicationTable()
        {
            for (int i = 1; i <= 9; i++)
            {
                for (int j = 1; j <= 9; j++)
                {
                    MultiplicationListBox.Items.Add($"{i} × {j} = {i * j}");
                }
                // 每個乘數之間加空行
                MultiplicationListBox.Items.Add("");
            }
        }
    }
}
