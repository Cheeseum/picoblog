/*global module:false*/
module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    // Metadata.
    pkg: grunt.file.readJSON('package.json'),
    banner: '/*! <%= pkg.title || pkg.name %> - v<%= pkg.version %> - ' +
      '<%= grunt.template.today("yyyy-mm-dd") %>\n' +
      '<%= pkg.homepage ? "* " + pkg.homepage + "\\n" : "" %>' +
      '* Copyright (c) <%= grunt.template.today("yyyy") %> <%= pkg.author.name %>;' +
      ' License: <%= pkg.license %> */\n',

    // Directories
    staticdir: '<%= pkg.name %>/static/<%= pkg.name %>',
    templatedir: '<%= pkg.name %>/templates/<%= pkg.name %>',

    // Task configuration.
    copy: {
        dist: {
            files: [{
                src : ['<%= pkg.name %>/**/*.py', 'manage.py'],
                dest: 'dist/'
            }]
        }
    },
    remove: {
        dist: {
            dirList: ['build/', 'dist/']
        }
    },
    concat: {
      options: {
        banner: '<%= banner %>',
        stripBanners: true
      },
      css: {
        src: ['<%= staticdir %>/css/*.css'],
        dest: 'build/<%= staticdir %>/css/style.combined.css'
      },
      dist: {
        src: ['<%= staticdir %>/js/*.js'],
        dest: 'build/<%= staticdir %>/js/<%= pkg.name %>.js'
      }
    },
    uglify: {
      options: {
        banner: '<%= banner %>'
      },
      dist: {
        src: '<%= concat.dist.dest %>',
        dest: 'dist/<%= staticdir %>/js/<%= pkg.name %>.min.js'
      }
    },
    jshint: {
      options: {
        curly: true,
        eqeqeq: true,
        immed: true,
        latedef: true,
        newcap: true,
        noarg: true,
        sub: true,
        undef: true,
        unused: true,
        boss: true,
        eqnull: true,
        browser: true,
        globals: {}
      },
      gruntfile: {
        src: 'Gruntfile.js'
      }
    },
    sass: {
        compile: {
            options: {
                sourcemap: 'none'
            },
            files: [{
                expand: true,
                flatten: true,
                src: ['<%= staticdir %>/scss/*.scss'],
                dest: '<%= staticdir %>/css/',
                ext: '.css'
            }]
        }
    },
    cssmin: {
        options: {
            banner: '<%= banner %>'
        },
        dist: {
            files: [{
                expand: true,
                cwd: 'build/',
                src: ['<%= staticdir %>/css/*.css'],
                dest: 'dist/',
                ext: '.min.css'
            }]
        }
    },
    processhtml: {
        dist: {
            files: [{
                expand: true,
                src: '<%= templatedir %>/*.html',
                dest: 'dist/'
            }]
        }
    },
    watch: {
      gruntfile: {
        files: '<%= jshint.gruntfile.src %>',
        tasks: ['jshint:gruntfile']
      },
      css: {
        files: '**/*.scss',
        tasks: ['sass']
      }
    }
  });

  // These plugins provide necessary tasks.
  grunt.loadNpmTasks('grunt-remove');
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-css');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-processhtml');
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Default task.
  grunt.registerTask('build', ['jshint', 'sass']);
  grunt.registerTask('dist', ['remove:dist', 'build', 'concat', 'uglify', 'cssmin', 'processhtml', 'copy:dist']);
  grunt.registerTask('publish', ['dist']);
  grunt.registerTask('default', ['watch']);
};
