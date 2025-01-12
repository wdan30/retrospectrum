#pragma once

#include <complex>
#include <vector>

using namespace std;

class Candidate {
private:
	vector<Wave> waves;
};

class Wave {
private:
	vector<complex<float>> fourier;

public:
	void with_triangle_wave(int fundamental) {
		int numHarmonics = 10;

		for(int i = 0; i < numHarmonics)
	}

};