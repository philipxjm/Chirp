var gulp = require('gulp');
var sass = require('gulp-sass');
var uglify = require('gulp-uglify');
var autoprefixer = require('gulp-autoprefixer');
var cleancss = require('gulp-clean-css');
var sourcemaps = require('gulp-sourcemaps');
var pump = require('pump');
var preprocess = require('gulp-preprocess');
var serve = require('gulp-serve');
var flatten = require('gulp-flatten');
var livereload = require('gulp-livereload');

// tasks
gulp.task('compilehtml', function(cb) {
	pump([
		gulp.src('src/html/*.html'),
		preprocess(),
		gulp.dest('../chirp/assets/'),
		livereload()
	], cb);
});

gulp.task('copylibs', function() {
	return gulp.src('src/lib/**')
		.pipe(gulp.dest('../chirp/assets/js/lib/'));
});

gulp.task('copyvis', function() {
	return gulp.src('src/vis/**')
		.pipe(gulp.dest('../chirp/assets/js/vis/'));
});

gulp.task('copydata', function() {
	return gulp.src('src/data/**')
		.pipe(gulp.dest('../chirp/assets/data/'));
});

gulp.task('compilejs', function(cb) {
	pump([
		gulp.src('src/js/*'),
		//		uglify(),
		gulp.dest('../chirp/assets/js/'),
		livereload()
	], cb);
})

gulp.task('compilescss', function(cb) {
	pump([
		gulp.src('src/scss/*'),
		sourcemaps.init(),
		sass(),
		autoprefixer({
			browsers: ['last 2 versions'],
			cascade: false
		}),
		cleancss(),
		sourcemaps.write(),
		gulp.dest('../chirp/assets/css/'),
		livereload()
	], cb);
});

gulp.task('watch', function() {
	livereload.listen();
	gulp.watch('src/js/**', ['compilejs']);
	gulp.watch('src/html/*', ['compilehtml']);
	gulp.watch('src/scss/**', ['compilescss']);
	gulp.watch('src/libs/*', ['copylibs']);
	gulp.watch('src/vis/*', ['copyvis']);
	gulp.watch('src/data/*', ['copydata']);
})

gulp.task('serve', serve('../chirp/assets/'));

gulp.task('build', [
	'compilejs',
	'compilescss',
	'copylibs',
	'compilehtml',
	'copyvis',
	'copydata'
])

gulp.task('default', [
	'compilejs',
	'compilescss',
	'copylibs',
	'copyvis',
	'copydata',
	'compilehtml',
	'watch',
	'serve'
]);
