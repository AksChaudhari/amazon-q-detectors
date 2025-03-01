// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

// {fact rule=cpp-unreleased-lock@v1.0 defects=1}
#include <iostream>
#include <mutex>

using namespace std;

std::mutex a_mutex;

bool doWork() {
    return true;
}

int compliant() {
    a_mutex.lock();
    bool succeeded = doWork();
    if (!succeeded) {
        // Noncompliant: Presence of a branch with the following acquired lock is not released. 
        return -1;
    }
    a_mutex.unlock();
    return 1;
}
// {/fact}
