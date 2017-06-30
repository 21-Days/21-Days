Sk.externalLibraries = {
	numpy : {
		path: 'http://example.com/static/primeronoo/skulpt/external/numpy/__init__.js',
		dependencies: ['/static/primeronoo/skulpt/external/deps/math.js'],
	},
	matplotlib : {
		path: '/static/primeronoo/skulpt/external/matplotlib/__init__.js'
	},
	"matplotlib.pyplot" : {
		path: '/static/primeronoo/skulpt/external/matplotlib/pyplot/__init__.js',
		dependencies: ['/static/primeronoo/skulpt/external/deps/d3.min.js'],
	},
	"arduino": {
		path: '/static/primeronoo/skulpt/external/arduino/__init__.js'
	}
};
