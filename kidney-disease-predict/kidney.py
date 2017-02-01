import matplotlib.pyplot as plt

Counter = {
"Other":2.3,
"Other":2.3,
"GN":1.9,
"GN":1.9,
"Other":1.2,
"Other":1.2,
"Other":0.5,
"Other":0.5,
"Other":1.5,
"Other":1.5,
"Other":1.1,
"Other":1.1,
"GN":3,
"GN":3,
"GN":0.5,
"GN":0.5,
"AN":0.7,
"AN":0.7,
"GN":0.4,
"GN":0.4,
"AN":0.6,
"AN":0.6,
"Other":1.2,
"Other":1.2,
"AN":1.4,
"AN":1.4,
"AN":0.4,
"AN":0.4,
"Other":0.4,
"Other":0.4,
"AN":1.1,
"AN":1.1,
"Other":0.8,
"Other":0.8,
"Other":0.8,
"GN":0.5,
"GN":0.5,
"Other":1.3,
"Other":1.3,
"PKD":0.2,
"Other":0.6,
"Other":0.6,
"AN":1.7,
"AN":1.7,
"AN":1,
"AN":0.7,
"AN":0.7,
"AN":0.5,
"AN":0.5,
"GN":1.1,
"GN":1.1,
"AN":1.8,
"AN":1.8,
"GN":1.5,
"GN":1.5,
"GN":1.5,
"AN":1.7,
"AN":1.7,
"AN":1.3,
"AN":1.3,
"PKD":2.9,
"PKD":2.9,
"GN":0.7,
"GN":0.7,
"Other":2.2,
"Other":2.2,
"Other":0.7,
"Other":0.7,
"PKD":2.1,
"PKD":2.1,
"PKD":1.2,
"PKD":1.2,
}

#Plot bar with values from dict and label with keys
plt.bar(range(len(Counter)), Counter.values(), align='center')
plt.xticks(range(len(Counter)), Counter.keys())

#Rotate labels by 90 degrees so you can see them
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)

plt.show()

def free_energy_profile_V(lnhz):
    F = np.zeros(lnhz.shape[0] - lnhz.shape[1] + 3)
    lnhzmax_V = np.zeros(lnhz.shape[0] - lnhz.shape[1] + 3)
    for i in range(lnhz.shape[0]):
        for j in range(lnhz.shape[1]):
            V = i - j + 1
            if np.isfinite(lnhz[i,j]) and lnhz[i,j] > lnhzmax_V[V]:
                lnhzmax_V[V] = lnhz[i,j]
    for i in range(lnhz.shape[0]):
        for j in range(lnhz.shape[1]):
            V = i - j + 1
            if np.isfinite(lnhz[i,j]):
                F[V] += math.exp(lnhz[i,j] - lnhzmax_V[V])
    for V in range(1, len(F)):
        F[V] = -math.log(F[V]) - lnhzmax_V[V]


        def run(out_dir, config_fname, data_paths_fname, stats_list_fname, split_fname=None, check_if_file_exists=False, verbose=True): 

        	data_paths = util.read_yaml(data_paths_fname)
        	config = util.read_yaml(config_fname)

        	stats_key = config['stats_key']
        	outcome_stat_name = config['outcome_stat_name']
        	cohort_stat_name = config.get('cohort_stat_name', None)
        	lab_lower_bound = config.get('lab_lower_bound', None)
        	lab_upper_bound = config.get('lab_upper_bound', None)
        	gap_days = config.get('gap_days', None)
        	training_window_days = config['training_window_days']
        	buffer_window_days = config['buffer_window_days']
        	outcome_window_days = config['outcome_window_days']
        	time_period_days = config['time_period_days']
        	time_scale_days = config['time_scale_days']
        	use_just_labs = config['use_just_labs']
        	feature_loincs_fname = config['feature_loincs_fname']
        	add_age_sex = config['add_age_sex']
        	calc_gfr = config['calc_gfr']
        	regularizations = config.get('regularizations', [1])
        	lin_n_cv_iters = config.get('lin_n_cv_iters', -1)
        	n_cv_iters = config.get('n_cv_iters', -1)
        	progression = config['progression']
        	progression_lab_lower_bound = config.get('progression_lab_lower_bound', None)
        	progression_lab_upper_bound = config.get('progression_lab_upper_bound', None)
        	progression_gap_days = config.get('progression_gap_days', None)
        	progression_stages = config.get('progression_stages', None)
        	progression_init_stages = config.get('progression_init_stages', None)
        	evaluate_nn = config.get('evaluate_nn', True)

        	outcome_fname = out_dir + stats_key + '_' + outcome_stat_name + '.txt'
        	if cohort_stat_name is None:
        		cohort_fname = data_paths['demographics_fname']	
        	else:
        		cohort_fname = out_dir + stats_key + '_' + cohort_stat_name + '.txt'
        	gfr_loincs = util.read_list_files('data/gfr_loincs.txt')
        	training_data_fname = out_dir + stats_key + '_training_data.txt'

        	feature_loincs = util.read_list_files(feature_loincs_fname)
        	if use_just_labs == False:
        		feature_diseases = [[icd9] for icd9 in util.read_list_files('data/kidney_disease_mi_icd9s.txt')]
        		feature_drugs = [util.read_list_files('data/drug_class_'+dc.lower().replace('-','_').replace(',','_').replace(' ','_')+'_ndcs.txt') for dc in util.read_list_files('data/kidney_disease_drug_classes.txt')]
        	else: 
        		feature_diseases = []	
        		feature_drugs = []

        	n_labs = len(feature_loincs)

        	if add_age_sex:
        		age_index = len(feature_loincs) + len(feature_diseases) + len(feature_drugs)
        		gender_index = len(feature_loincs) + len(feature_diseases) + len(feature_drugs) + 1
        	else:
        		age_index = None
        		gender_index = None

        	features_fname = out_dir + stats_key + '_features.h5'
        	features_split_fname = out_dir + stats_key + '_features_split.h5'
        	predict_fname = out_dir + stats_key + '_prediction_results.yaml'
        	if evaluate_nn:
        		nn_predict_fname = out_dir + stats_key + '_nn_prediction_results.yaml'
        	else:
        		nn_predict_fname = None

        	if verbose:
        		print "Loading data"

        	db = util.Database(data_paths_fname)
        	db.load_people()
        	db.load_db(['loinc','loinc_vals','cpt','icd9_proc','icd9','ndc'])

        	stats = util.read_yaml(stats_list_fname)[stats_key]

        	if verbose:
        		print "Calculating patient stats"

        	data = ps.patient_stats(db, stats, stats_key, out_dir, stat_indices=None, verbose=verbose, check_if_file_exists=check_if_file_exists, save_files=True)

        	if verbose:
        		print "Building training data"

        	outcome_data = btd.build_outcome_data(out_dir, outcome_fname)
        	cohort_data = btd.setup(data_paths['demographics_fname'], outcome_fname, cohort_fname)
        	# calc_gfr = True here because it's required to define the condition
        	training_data = btd.build_training_data(db, cohort_data, gfr_loincs, lab_lower_bound, lab_upper_bound, \
        		training_window_days, buffer_window_days, outcome_window_days, time_period_days, time_scale_days, gap_days, calc_gfr=True, verbose=verbose, \
        		progression=progression, progression_lab_lower_bound=progression_lab_lower_bound, progression_lab_upper_bound=progression_lab_upper_bound, \
        		progression_gap_days=progression_gap_days, progression_init_stages=progression_init_stages, progression_stages=progression_stages)
        	training_data.to_csv(training_data_fname, index=False, sep='\t')

        	if verbose:
        		print "Building features"

        	features.features(db, training_data, feature_loincs, feature_diseases, feature_drugs, time_scale_days, features_fname, calc_gfr, verbose, add_age_sex)

        	if split_fname is None:
        		split_fname = out_dir + stats_key + '_split.txt'
        		features.train_validation_test_split(training_data['person'].unique(), split_fname, verbose=verbose)

        	features.split(features_fname, features_split_fname, split_fname, verbose)
        	
        	if verbose:
        		print "Training, validating and testing models"

        	predict.predict(features_split_fname, lin_n_cv_iters, n_cv_iters, regularizations, n_labs, age_index, gender_index, predict_fname, nn_predict_fname)

