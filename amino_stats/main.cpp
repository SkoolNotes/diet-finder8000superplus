#include <iostream>
#include <string>
#include <array>
#include <map>

const size_t LETTERS = 26;
const size_t LINECOUNT = 4224493;
const size_t UPDATE_PERIOD = 100000;
const std::string FILENAME = "data_processed.txt";

typedef std::array<size_t, LETTERS> Statistic;

std::map<std::string, Statistic> stats;

int main()
{
    //FILE* f = fopen("data_processed.fasta", "r");
    // TODO: \/ freopen because idk how getline works on files gang
    if (!fopen(FILENAME.c_str(), "r"))
    {
        printf("File not found!\n");
        return 1;
    }
    freopen(FILENAME.c_str(), "r", stdin);
    std::string inp, name;
    for (size_t ln=0; ln<LINECOUNT; ++ln)
    {
        for (int r=0; r<UPDATE_PERIOD-1 && ln<LINECOUNT; ++ln, ++r)
        {
            getline(std::cin, inp);
            if (inp[0] == '>') std::swap(name, inp);
            else for (char c : inp) ++stats[name][c-'A'];
        }
        printf("ln = %10d of %10d (%.1lf%%)   \r", ln, LINECOUNT, (double)ln/(double)LINECOUNT*100);
    }

    FILE* out = fopen("statistics.txt", "w+");
    for (auto p : stats)
    {
        fprintf(out, "%s:\n", p.first.c_str());
        for (size_t i=0; i<LETTERS; ++i) if (p.second[i])
            fprintf(out, "    %c: %lu\n", i+'A', p.second[i]);
    }
}

