###########################################################################################################################################################
# DLL INJECTION
// OPEN_PROCESS
[DllImport("kernel32.dll", SetLastError = true)]
public static extern IntPtr OpenProcess(uint processAccess, bool bInheritHandle, int processId);
  
// VIRTUAL_ALLOC_EX
[DllImport("kernel32.dll", SetLastError=true, ExactSpelling=true)]
static extern IntPtr VirtualAllocEx(IntPtr hProcess, IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);

// WRITE_PROCESS_MEMORY
[DllImport("kernel32.dll")]
static extern bool WriteProcessMemory(IntPtr hProcess, IntPtr lpBaseAddress, byte[] lpBuffer, Int32 nSize, out IntPtr lpNumberOfBytesWritten);

// CREATE_REMOTE_THREAD
[DllImport("kernel32.dll")]
static extern IntPtr CreateRemoteThread(IntPtr hProcess, IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);

// GET_PROC_ADDRESS
[DllImport("kernel32", CharSet=CharSet.Ansi, ExactSpelling=true, SetLastError=true)]
static extern IntPtr GetProcAddress(IntPtr hModule, string procName);

// GET_MODULE_HANDLE
[DllImport("kernel32.dll", CharSet=CharSet.Unicode, SetLastError=true)]
public static extern IntPtr GetModuleHandle([MarshalAs(UnmanagedType.LPWStr)] in string lpModuleName);
###########################################################################################################################################################
# ANTIVIRUS
// VIRTUAL_ALLOC
  [DllImport("kernel32")]
  public static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);

// CREATE_THREAD
[DllImport("kernel32", CharSet = CharSet.Ansi)]
    public static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);

// WAIT_FOR_SIN>GLE_OBJECT
[DllImport("kernel32.dll", SetLastError=true)]
  static extern UInt32 WaitForSingleObject(IntPtr hHandle, UInt32 dwMilliseconds);

