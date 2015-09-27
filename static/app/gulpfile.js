var gulp = require('gulp'),
	ts   = require('gulp-typescript'),
	del  = require('del');
	
var tsCompilerOptions = {
        noImplicitAny: true,
        rootDir: '.',
        module: 'commonjs',
        jsx: 'react'
      };

gulp.task('kno-app', function () {
  var tsResult = gulp.src('scripts/**/*.tsx')
    .pipe(ts(tsCompilerOptions));
  return tsResult.js.pipe(gulp.dest('built/scripts'));
});	
	
gulp.task('clean', function(callback) {
  del(['built'], callback);
});