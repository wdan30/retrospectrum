#include "openGA.hpp"
#include <vector>;
#include <random>;
#include <math.h>;

const std::vector<double> target_amps;
const std::vector<double> target_phases;

/**
* WaveType - the type of wave
* fundamental - the fundamental frequency
* amplitude - the amplitude (>= 0)
*/
struct Wave
{
	int type;
	int note;
	double amplitude;
};

class Candidate
{
public:
	std::vector<Wave> waves;
	int count;

	Candidate(int count)
	{
		this->count = count;
		waves = std::vector<Wave>(count);
	}

	static Wave random_wave()
	{
		const long max_rand = 1000000L;
		double lower = 0.001;
		double upper = 1;
		double random_amp = lower + (upper - lower) * (rand() % max_rand) / max_rand;

		return Wave{rand() % 4, rand() % 88, random_amp};
	}

	static std::vector<double> triangle_amps(double fundamental, double amplitude)
	{
		std::vector<double> harm_amps;

		for (int i = 1; fundamental * i < 15000; ++i)
		{
			if (i % 2 == 0)
			{
				harm_amps.push_back(0);
			}
			else
			{
				harm_amps.push_back(amplitude * 8 / (i * i * 3.14 * 3.14));
			}
		}

		return harm_amps;
	}

	static std::vector<double> saw_amps(double fundamental, double amplitude)
	{
		std::vector<double> harm_amps;

		for (int i = 1; fundamental * i < 15000; ++i)
		{
			harm_amps.push_back(1 / (3.14 * i));
		}

		return harm_amps;
	}

	static std::vector<double> square_amps(double fundamental, double amplitude)
	{
		std::vector<double> harm_amps;

		for (int i = 1; fundamental * i < 15000; ++i)
		{
			harm_amps.push_back(i % 2 == 0 ? 0 : 4 / (3.14 * i));
		}

		return harm_amps;
	}
};



struct MiddleCost
{
	double amplitudeDist;
	double phaseDist;
};

void init_genes(Candidate& cand, std::function<double(void)> &rnd01)
{
	for (int i = 0; i < cand.count; ++i)
	{
		cand.waves.push_back(Candidate::random_wave());
	}
}

bool eval_solution(const Candidate& cand, MiddleCost& cost)
{
	std::vector<Wave> waves = cand.waves;
}

