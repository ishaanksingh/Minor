#include <iostream>
#include <string>

using namespace std;

int main() {
    int totalCases = 3;
    int totalParameters = 5;
    int parameterCounts[5] = {0};

    cout << "RAPID VISUAL SCREEN MODEL CREATED BY ISHANK SINGH\n";
    cout << "ENTER THE FOLLOWING PARAMETERS IN THE FORM OF YES/NO:\n";
    cout << "1) Is the building symmetrical?\n";
    cout << "2) Is the building having too slender members?\n";
    cout << "3) Is the building have U V T H joints?\n";
    cout << "4) Building has exterior plan dimension smaller at the plinth level than at upper storeys?\n";
    cout << "5) Building has heavier upper storeys\n";
    cout << "\n";

    for (int i = 0; i < totalCases; ++i) {
        cout << "Enter parameters for case " << i + 1 << " (yes/no):\n";
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

    cout << "Parameter Occurrence (%):\n";
    for (int j = 0; j < totalParameters; ++j) {
        double percentage = static_cast<double>(parameterCounts[j]) / totalCases * 100;
        cout << "Parameter " << j + 1 << ": " << percentage << "%" << endl;
    }

    return 0;
}