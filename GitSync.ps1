powershell
# Git Branch Synchronization Script
# This script synchronizes changes between dev and main branches

param(
    [switch]$Verbose = $false,
    [switch]$Force = $false
)

function Write-Log {
    param([string]$Message, [string]$Level = "INFO")
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Level] $Message"
}

function Test-BranchDifferences {
    try {
        # Check if there are differences between main and dev
        $diffResult = git diff --name-only main dev 2>$null
        if ($diffResult) {
            Write-Log "Differences found between main and dev:"
            $diffResult | ForEach-Object { Write-Log $_ "DETAIL" }
            return $true
        } else {
            Write-Log "No differences found - branches are identical"
            return $false
        }
    } catch {
        Write-Log "Error checking branch differences: $($_.Exception.Message)" "ERROR"
        return $false
    }
}

function Invoke-Synchronization {
    Write-Log "Initiating Git branch synchronization process..."
    
    # Check current branch
    try {
        $currentBranch = git rev-parse --abbrev-ref HEAD 2>$null
        Write-Log "Current branch: $currentBranch"
    } catch {
        Write-Log "Could not determine current branch" "ERROR"
        return
    }
    
    # Get latest changes from remote
    Write-Log "Fetching latest changes from origin..."
    try {
        git fetch origin
    } catch {
        Write-Log "Error fetching from origin: $($_.Exception.Message)" "ERROR"
        return
    }
    
    # Verify we're on dev branch (required for synchronization)
    if ($currentBranch -ne "dev") {
        Write-Log "Warning: Current branch is '$currentBranch', not 'dev'" "WARN"
        Write-Log "Synchronization should be performed from dev branch" "WARN"
        
        if (-not $Force) {
            Write-Log "Exiting due to branch mismatch. Use -Force to override." "INFO"
            return
        }
    }
    
    # Check for differences
    $hasDifferences = Test-BranchDifferences
    
    # Perform synchronization based on differences
    if ($hasDifferences) {
        Write-Log "Branches differ - synchronization needed"
        Write-Log "Performing merge from main to dev..."
        
        try {
            # Ensure we're on dev branch
            git checkout dev
            
            # Pull latest changes from dev branch
            git pull origin dev
            
            # Merge main into dev
            git merge main
            
            Write-Log "Merge completed successfully!"
            
            # Check if there are uncommitted changes after merge
            $status = git status --porcelain 2>$null
            if ($status) {
                Write-Log "Uncommitted changes detected. Please review before proceeding." "WARN"
                $status | ForEach-Object { Write-Log $_ "DETAIL" }
            } else {
                Write-Log "No uncommitted changes detected. Merge ready for commit."
            }
            
        } catch {
            Write-Log "Error during merge: $($_.Exception.Message)" "ERROR"
            return
        }
    } else {
        Write-Log "No differences found between branches - synchronization not needed"
        
        # Ensure we're on dev branch
        if ($currentBranch -ne "dev") {
            try {
                git checkout dev
                Write-Log "Switched to dev branch for sync operation"
            } catch {
                Write-Log "Could not switch to dev branch: $($_.Exception.Message)" "ERROR"
            }
        }
    }
    
    # Show final status
    Write-Log "Final Git status:"
    try {
        git status --branch
    } catch {
        Write-Log "Error getting final status: $($_.Exception.Message)" "ERROR"
    }
}

# Main execution
Invoke-Synchronization