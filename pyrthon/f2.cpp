#include <iostream>
#include <libxl.h>

using namespace libxl;

int main() {
    Book* book = xlCreateXMLBook();
    if (book) {
        if (book->load("parameters.xlsx")) { // Load your Excel file here
            Sheet* sheet = book->getSheet(0); // Assuming the parameters are in the first sheet

            if (sheet) {
                int totalCases = sheet->lastRow() - 1; // Assuming the first row is for headers
                int totalParameters = sheet->lastCol();

                int parameterCounts[5] = {0};

                for (int i = 1; i <= totalCases; ++i) {
                    for (int j = 0; j < totalParameters; ++j) {
                        const wchar_t* cellValue = sheet->readStr(i, j + 1);
                        string parameter = utf8FromWide(cellValue);

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
            } else {
                cerr << "Error: Unable to access the Excel sheet." << endl;
            }

            book->release();
        } else {
            cerr << "Error: Unable to load the Excel file." << endl;
        }
    } else {
        cerr << "Error: Unable to create a book." << endl;
    }

    return 0;
}