# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.12

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = "/Users/isabey/Library/Application Support/JetBrains/Toolbox/apps/CLion/ch-0/182.4505.18/CLion.app/Contents/bin/cmake/mac/bin/cmake"

# The command to remove a file.
RM = "/Users/isabey/Library/Application Support/JetBrains/Toolbox/apps/CLion/ch-0/182.4505.18/CLion.app/Contents/bin/cmake/mac/bin/cmake" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/isabey/CLionProjects/CS288

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/isabey/CLionProjects/CS288/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/CS288.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/CS288.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/CS288.dir/flags.make

CMakeFiles/CS288.dir/Unit1/main.cpp.o: CMakeFiles/CS288.dir/flags.make
CMakeFiles/CS288.dir/Unit1/main.cpp.o: ../Unit1/main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/isabey/CLionProjects/CS288/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/CS288.dir/Unit1/main.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/CS288.dir/Unit1/main.cpp.o -c /Users/isabey/CLionProjects/CS288/Unit1/main.cpp

CMakeFiles/CS288.dir/Unit1/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/CS288.dir/Unit1/main.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/isabey/CLionProjects/CS288/Unit1/main.cpp > CMakeFiles/CS288.dir/Unit1/main.cpp.i

CMakeFiles/CS288.dir/Unit1/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/CS288.dir/Unit1/main.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/isabey/CLionProjects/CS288/Unit1/main.cpp -o CMakeFiles/CS288.dir/Unit1/main.cpp.s

# Object files for target CS288
CS288_OBJECTS = \
"CMakeFiles/CS288.dir/Unit1/main.cpp.o"

# External object files for target CS288
CS288_EXTERNAL_OBJECTS =

CS288: CMakeFiles/CS288.dir/Unit1/main.cpp.o
CS288: CMakeFiles/CS288.dir/build.make
CS288: CMakeFiles/CS288.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/isabey/CLionProjects/CS288/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable CS288"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/CS288.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/CS288.dir/build: CS288

.PHONY : CMakeFiles/CS288.dir/build

CMakeFiles/CS288.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/CS288.dir/cmake_clean.cmake
.PHONY : CMakeFiles/CS288.dir/clean

CMakeFiles/CS288.dir/depend:
	cd /Users/isabey/CLionProjects/CS288/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/isabey/CLionProjects/CS288 /Users/isabey/CLionProjects/CS288 /Users/isabey/CLionProjects/CS288/cmake-build-debug /Users/isabey/CLionProjects/CS288/cmake-build-debug /Users/isabey/CLionProjects/CS288/cmake-build-debug/CMakeFiles/CS288.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/CS288.dir/depend

