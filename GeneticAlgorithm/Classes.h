#pragma once

#include <complex>
#include <vector>

using namespace std;

enum WaveType {
	Sine,
	Triangle,
	Square,
	Saw
};

/*
class Candidate {
private:
	vector<Wave> waves;
	vector<float> amplitudes = vector<float>{ 15000, 0 };

public:
	void calculateAmplitudes() {
		for (int i = 0; i < waves.size(); ++i) {
			waves[i].addWave();
		}
	}
};
*/

class Wave {
private:
	WaveType waveType;
	double fundamental;
	double amplitude;

public:
	Wave(double fundamental, double amplitude) {
		this->fundamental = fundamental;
		this->amplitude = amplitude;
	}

	vector<float> addWave() {
		if (waveType == Sine) {
			for (int freq = fundamental; freq <= 15000; freq += fundamental) {

			}
		}
	}

	WaveType getWaveType() {
		return waveType;
	}
};