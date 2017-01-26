import lung_sim 
stripes=[1,2,4,10]
lung_sim.plot_stripes(stripes, 100)
time_list = lung_sim.run_multi_model(stripes)
lung_sim.histogram_all(time_list, stripes)
