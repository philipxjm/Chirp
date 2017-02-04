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
		gulp.dest('../chirp/static/'),
		livereload()
	], cb);
});

gulp.task('copylibs', function() {
	return gulp.src('src/lib/**')
		.pipe(gulp.dest('../chirp/static/js/lib/'));
});

gulp.task('compilejs', function(cb) {
	pump([
		gulp.src('src/js/*'),
		//		uglify(),
		gulp.dest('../chirp/static/js/')
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
		gulp.dest('../chirp/static/css/')
	], cb);
});

gulp.task('watch', function() {
	livereload.listen();
	gulp.watch('src/js/**', ['compilejs']);
	gulp.watch('src/html/*', ['compilehtml']);
	gulp.watch('src/scss/**', ['compilescss']);
	gulp.watch('src/libs/*', ['copylibs']);
})

gulp.task('serve', serve('../chirp/static/'));

gulp.task('build', [
	'compilejs',
	'compilescss',
	'copylibs',
	'compilehtml',
])

gulp.task('default', [
	'compilejs',
	'compilescss',
	'copylibs',
	'compilehtml',
	'watch',
	'serve'
]);
