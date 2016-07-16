var gulp = require('gulp');

// plugins
var fs     = require('fs');
var path   = require('path');
var es     = require('event-stream');
var jshint = require('gulp-jshint');
var sass   = require('gulp-sass');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');

var startPath = 'shout_webapp/frontend-dev';
var finalPath = 'shout_webapp/frontend-dist';

function getFolders(dir) {
	return fs.readdirSync(dir)
			.filter(function(file) {
					return fs.statSync(path.join(dir, file)).isDirectory();
			});
}

gulp.task('lint', function() {
	return gulp.src('shout_webapp/frontend-dev/scripts/*.js')
		.pipe(jshint())
		.pipe(jshint.reporter('default'));
});

gulp.task('sass', function() {
	return gulp.src('shout_webapp/frontend-dev/scss/*.scss')
		.pipe(sass())
		.pipe(gulp.dest(finalPath + '/css/'));
});

// concat and minify/uglify
gulp.task('scripts', function() {
	var folders = getFolders(startPath);

	var tasks = folders.map(function(folder) {
		return gulp.src(path.join(startPath, folder, '/*.js'))
			.pipe(concat(folder + '.js'))
			.pipe(gulp.dest(finalPath + '/js'));
	});

	return es.concat.apply(null, tasks);
});

gulp.task('watch', function() {
	gulp.watch('shout_webapp/scripts/*.js', ['lint', 'scripts']);
	gulp.watch('shout_webapp/static/*.scss', ['sass']);
});

gulp.task('default', ['lint', 'sass', 'scripts', 'watch']);