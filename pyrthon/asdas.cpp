#include <iostream>
#include <string>

using namespace std;

int main() {
    int totalCases = 3;
    int totalParameters = 5;
    int parameterCounts[5] = {0};

    for (int i = 0; i < totalCases; ++i) {
        cout << "Enter parameters for case " << i + 1 << " (yes/no):" << endl;
        for (int j = 0; j < totalParameters; ++j) {
            string parameter;
            do {
                cout << "Parameter " << j + 1 << ": ";
                cin >> parameter;
            } while (parameter != "yes" && parameter != "no");
            
            if (parameter == "yes") {
                parameterCounts[j]++;
            }
        }
    }

    cout << "Parameter Occurrence (%):" << endl;
    for (int j = 0; j < totalParameters; ++j) {
        double percentage = static_cast<double>(parameterCounts[j]) / totalCases * 100;
        cout << "Parameter " << j + 1 << ": " << percentage << "%" << endl;
    }

    return 0;
}