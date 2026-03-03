import asyncio
import threading
import multiprocessing
import time
import math

# 1. Asyncio:
async def check_server_latency(server_id):
    print(f"[Asyncio] Pinging Server {server_id}...")
    await asyncio.sleep(1)  
    print(f"[Asyncio] Server {server_id} is online.")
    return f"Server_{server_id}_OK"

async def run_asyncio_tasks():
    print("--- Starting Asyncio (Network Tasks) ---")
    start_time = time.time()
    
    #(Concurrent)
    tasks = [check_server_latency(i) for i in range(1, 4)]
    results = await asyncio.gather(*tasks)
    
    print(f"Asyncio Results: {results}")
    print(f"Asyncio Time: {time.time() - start_time:.2f} seconds\n")

# 2. Threading:
def load_weapon_animation(anim_name):
    print(f"[Thread] Loading animation: {anim_name}...")
    time.sleep(1)  
    print(f"[Thread] Animation '{anim_name}' loaded.")

def run_threading_tasks():
    print("--- Starting Threading (File I/O Tasks) ---")
    start_time = time.time()
    
    animations = ["idle.fbx", "reload_30_bullets.fbx", "shoot.fbx"]
    threads = []
    
    for anim in animations:
        t = threading.Thread(target=load_weapon_animation, args=(anim,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()  # รอให้ทุก Thread ทำงานเสร็จ
        
    print(f"Threading Time: {time.time() - start_time:.2f} seconds\n")

# 3. Process Pool: 
def calculate_bullet_physics(trajectory_id):
    # ปิด print เพื่อไม่ให้ Git Bash ค้าง
    # print(f"[Process] Calculating bullet physics for ID: {trajectory_id}...")
    result = sum(math.sqrt(i) for i in range(5_000_000))
    # print(f"[Process] Physics ID {trajectory_id} calculated.")
    return trajectory_id, result

def run_process_pool_tasks():
    print("--- Starting Process Pool (CPU Bound Tasks) ---")
    start_time = time.time()
    
    trajectories = [101, 102, 103]
    
    
    with multiprocessing.Pool(processes=3) as pool:
        results = pool.map(calculate_bullet_physics, trajectories)
        
    print(f"Process Pool Results collected: {len(results)} items")
    print(f"Process Pool Time: {time.time() - start_time:.2f} seconds\n")

# Main Execution    
if __name__ == '__main__':
    print("=== Game Processing Simulator ===\n")
    
    # รัน Asyncio
    asyncio.run(run_asyncio_tasks())
    
    # รัน Threading
    run_threading_tasks()
    
    # รัน Process Pool
    run_process_pool_tasks()
    
    print("=== All systems go! ===")